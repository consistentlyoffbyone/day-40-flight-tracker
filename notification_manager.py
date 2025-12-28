import smtplib

from vonage import Auth, Vonage
from vonage_sms import SmsMessage, SmsResponse
from dotenv import load_dotenv
import os

load_dotenv()


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self._sms_api_key = os.environ["SMS_API_KEY"]
        self._sms_api_secret = os.environ["SMS_API_SECRET"]
        self._my_email = os.environ["MY_EMAIL"]
        self._my_password = os.environ["PASSWORD"]


    def send_sms(self, message_body):
        client = Vonage(Auth(api_key=self._sms_api_key, api_secret=self._sms_api_secret))
        message = SmsMessage(
            to="18563015327",
            from_="12393417993",
            text=message_body,
        )

        response: SmsResponse = client.sms.send(message)
        return response

    def send_emails(self, user_email, email_message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls() #make connection secure
            connection.login(user=self._my_email, password=self._my_password)
            connection.sendmail(
                from_addr=self._my_email,
                to_addrs=user_email,
                msg=email_message
            )