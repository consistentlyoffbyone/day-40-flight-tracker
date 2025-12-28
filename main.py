from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager
import smtplib



data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_sheet_info()

for row in sheet_data:
    if row['iataCode'] == "":
        row['iataCode'] = flight_search.get_iata(row['city']) #THIS IS WHERE I AM LOOKING FOR THE AITA
        iata = row['iataCode']



data_manager.update_iata()


# CHECK FLIGHTS
ORIGIN_CITY = "City:philadelphia_pa_us"

today = datetime.now()
tomorrow = today + timedelta(days=1)
six_months_from_today = today + timedelta(days=182)

email_list = []
user_emails = data_manager.get_emails()
for col in user_emails['users']:
    email_list.append(col['whatIsYourEmail?'])


for destination in sheet_data:

    flights = flight_search.check_flights(
        origin_city = ORIGIN_CITY,
        destination_city_code = destination['iataCode'],
        from_time = tomorrow,
        to_time = six_months_from_today,
    )




    try:
        outbound_time_of_departure_str = flights['itineraries'][0]['outbound']['sectorSegments'][0]['segment']['destination']['localTime']
        inbound_time_of_departure_str = flights['itineraries'][0]['inbound']['sectorSegments'][0]['segment']['destination']['localTime']
        datetime_object_out = datetime.fromisoformat(outbound_time_of_departure_str)
        datetime_object_in = datetime.fromisoformat(inbound_time_of_departure_str)
        out_date = datetime_object_out.strftime("%Y-%m-%d")
        return_date = datetime_object_in.strftime("%Y-%m-%d")

        cheapest_flight = int(flights['itineraries'][0]['price']['amount'])

        if cheapest_flight < destination['lowestPrice']:
            print(f"Lower price flight found to {destination['city']}!")
            notification_manager = NotificationManager()

            for email in email_list:
                notification_manager.send_emails(
                    user_email=email,
                    email_message=f"Subject:Low Price Alert!\n\nOnly ${cheapest_flight} to fly from Philadelphia, PA to {destination['city']}, on {out_date} until {return_date}.",
                )


            #notification_manager.send_sms(
                #message_body=f"Low Price Alert! Only ${cheapest_flight} to fly from {ORIGIN_CITY} to {destination['city']}, on {out_date} until {return_date}."
            #)




        else:
            print(f"Nothing cheaper for flights to {destination['city']} yet!")

    except TypeError:
        print("TypeError")






