# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

today = dt.datetime.today()
today_month = today.month
today_day = today.day
today = (today_month, today_day)
data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if ((today) in birthday_dict):
    birthday_email = birthday_dict[today]["email"]
    birthday_name = birthday_dict[today]["name"]

letter_list = random.randint(1,3)
letter = f"./letter_templates/letter_{letter_list}.txt"
with open(letter) as letter_file:
    letter = letter_file.read()
    letter = letter.replace("[NAME]", birthday_name)

my_email = "infotoerictangallery@gmail.com"
password = "ubetcnqvnrtoyvtg"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs={birthday_email},
                        msg=f"Subject:Happy birthday {birthday_name}\n\n{letter}"
                        )


