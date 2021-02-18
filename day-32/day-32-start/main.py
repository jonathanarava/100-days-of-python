# ------------------SMTPLIB-------------------------
# import smtplib
#
# my_email = "****@yahoo.com"
# password = "****"
#
# # creates an SMTP object with email provider's smtp server as parameter
# with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="****@gmail.com",
#                         msg="Subject:Hello\n\nBody of my email")

# ------------------DATETIME-------------------------
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15)
# print(date_of_birth)

# ------------------CHALLENGE 1-------------------------
"""Send motivational quotes on monday"""
import datetime as dt
import smtplib
import random

current_weekday = dt.datetime.now().weekday()

if current_weekday == 3:  # 3: Thursday, (monday = 0)

    # Gets random quote from file
    with open(file="quotes.txt", mode='r') as data_file:
        list_of_quotes = data_file.readlines()
        random_quote = random.choice(list_of_quotes)

    # Email setup
    my_email = "****@yahoo.com"
    my_password = "****"
    my_to_addrs = "****@gmail.com"

    # creates an SMTP object with email provider's smtp server as parameter
    # emails quote
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_to_addrs,
                            msg=f"Subject:Quote of the Day\n\n{random_quote}")
