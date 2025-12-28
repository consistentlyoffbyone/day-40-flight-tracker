import requests
from dotenv import load_dotenv
import os

load_dotenv()

# This class is responsible for talking to the Flight Search API.
class FlightSearch:
    def __init__(self):
        # For access key + cityCode
        self._city_code_api = os.environ["CITY_CODE_API"]
        self._city_code_api_secret = os.environ["CITY_CODE_API_SECRET"]
        self.AUTH_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

        # For Flight Search
        self._flight_api_key = os.environ["FLIGHT_API_KEY"]
        self._flight_api_host = os.environ["FLIGHT_API_HOST"]


    def get_access_token(self):
        header_token = {
            "content-type": "application/x-www-form-urlencoded"
        }

        secret_data = {
            "grant_type": "client_credentials",
            "client_id": self._city_code_api,
            "client_secret": self._city_code_api_secret,
        }

        response = requests.post(url=self.AUTH_ENDPOINT, data=secret_data, headers=header_token)
        access = response.json()
        token = access['access_token']
        return token



    def get_iata(self, city):

        headers = {
            "authorization": f"Bearer {self.get_access_token()}"
        }

        city_data = {
            "subType": "CITY,AIRPORT",
            "keyword": city,
        }

        response = requests.get(url="https://test.api.amadeus.com/v1/reference-data/locations",
                                     params=city_data,
                                     headers=headers
                                     )

        info = response.json()


        try:
            city_code = info['data'][0]['address']['cityCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city}")
            return N/A
        except KeyError:
            print(f"KeyError: No airport code found for {city}")
            return N/A

        return city_code



    def check_flights(self, origin_city, destination_city_code, from_time, to_time):

        headers = {
            "x-rapidapi-host": self._flight_api_host,
            "x-rapidapi-key": self._flight_api_key,
        }

        payload = {
            "source": origin_city,
            "destination": destination_city_code,
            "currency": "usd",
            "adults": "1",
            "cabinClass": "ECONOMY",
            "limit": "1",
            "outboundDepartmentDateStart": from_time.strftime("%Y-%m-%d"),
            "inboundDepartureDateStar": to_time.strftime("%Y-%m-%d"),
            "sortBy": "PRICE",

        }

        response = requests.get(url="https://kiwi-com-cheap-flights.p.rapidapi.com/round-trip", params=payload,
                                headers=headers)




        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search")
            print("Response body:", response.text)
            return None

        return response.json()

