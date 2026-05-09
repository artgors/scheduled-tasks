# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

from datetime import datetime as dt
import pandas
import random
import smtplib
import os
from email.message import EmailMessage

GMAIL_SMTP_SERVER = "smtp.gmail.com"
LETTER = "letter_1.txt"
BIRTHDAYS = "birthdays.csv"

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

actual_time = dt.datetime.now()
actual_month = actual_time.month
actual_day = actual_time.day

with open(BIRTHDAYS, mode="r") as file:
    birthdays = pandas.read_csv(file)
    birthdays_dictionary = {
        row["name"]: {
            "email":row["email"],
            "month":row["month"],
            "day":row["day"]
        } for _, row in birthdays.iterrows()}

    for key in birthdays_dictionary:
        if birthdays_dictionary[key]["month"] == actual_month and birthdays_dictionary[key]["day"] == actual_day:
            name = str(key)
            email = str(birthdays_dictionary[key]["email"])
            with open(LETTER, mode="r") as file:
                letter = file.read()
                updated_letter = letter.replace("[NAME]", name)
                email_message = EmailMessage()
                email_message["From"] = my_email
                email_message["To"] = my_email
                email_message["Subject"] = "Happy Birthday :)"
                email_message.set_content(updated_letter)
                with smtplib.SMTP(GMAIL_SMTP_SERVER, 587) as connection:
                    connection.starttls()
                    connection.login(my_email, password)
                    connection.send_message(email_message)
