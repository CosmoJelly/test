#Author: Waleed Nouman
#Roll-No: 21i2675
#Section: BS DS(U)

#importing libraries to use
import requests
import datetime as dt
#Date input system
year = int(input("Enter the year:"))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
#Date checking system
if ((year < 1900 or year > 2022) or (month > 12 or month < 0) or (day > 31 or day < 0)):
    print ("PROVIDED DATA IS INVALID")
    quit()
else:
    time_limit = dt.date(year, month, day)
#Taking currency codes for comversion
from_currency = str(input("Convert from: ")).upper()
to_currency = str(input("Convert to: ")).upper()
#Taking amount of currency to convert
amount = float(input("Enter amount: "))
#Checking if all arguments are present and correct
if ((from_currency == "") or (to_currency == "")):
    print("MISSING ARGUMENTS. PLEASE PROVIDE THEM IN THIS ORDER <DATE> <CURRENCY1> <CURRENCY2>")
    quit()
else:
    response1 = requests.get(f"https://api.frankfurter.app/{time_limit}?amount={amount}&from={from_currency}&to={to_currency}")
    print(f"{amount} {from_currency} is {response1.json()['rates'][to_currency]} {to_currency} in {time_limit}")
    print ("THE INVERSE CONVERSION RATE: ")
    response2 = requests.get(f"https://api.frankfurter.app/{time_limit}?amount={amount}&from={to_currency}&to={from_currency}")
    print(f"{amount} {to_currency} is {response2.json()['rates'][from_currency]} {from_currency} in {time_limit}")

    