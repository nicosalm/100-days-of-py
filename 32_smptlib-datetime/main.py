'''

import smtplib

MY_EMAIL = "removed for security reasons"
APP_PASSWORD = "removed for security reasons"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=APP_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, 
                        to_addrs="nico@varrix.dev", 
                        msg="Subject:Hello\n\nThis is the body of my email.")

'''

import datetime as dt

now = dt.datetime.now()

# break down the string
year = now.year
month = now.month
day_of_week = now.weekday()

# create a date object
date_of_birth = dt.datetime(year=1994, month=4, day=4, hour=12)

# create a time object
time_of_birth = dt.time(hour=12, minute=30, second=15)

if year == 2023:
    print("You were born this year.")
    
if date_of_birth.weekday() == 0:
    print("You were born on a Monday.")