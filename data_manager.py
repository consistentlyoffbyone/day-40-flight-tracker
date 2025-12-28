import requests
from dotenv import load_dotenv
import os

load_dotenv()


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._sheetly_price_sheet_url = os.environ["SHEETLY_PRICES_SHEET_URL"]
        self._sheetly_users_sheet_url = os.environ["SHEETLY_USERS_SHEET_URL"]
        self.destination_data = {}


    def get_sheet_info(self):
        response = requests.get(url=self._sheetly_price_sheet_url)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data


    def update_iata(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city['iataCode']
                }
            }

            results = requests.put(url=f"{self._sheetly_price_sheet_url}/{city['id']}", json=new_data)


    def get_emails(self):
        response = requests.get(url=self._sheetly_users_sheet_url)
        data = response.json()
        return data
