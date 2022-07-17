#Nawaal Fatima
#Oct 8, 2019
#Summ_WhileLoops.py
#Input prices from user and print tax, subtotal and total when ZERO is entered.

from datetime import date
from datetime import datetime

print()
print("Welcome to Azure Grocers!")
print("789 Whachamacallit Street")
print()
print("Cashier ID:57899")
print("Transaction Number:16782")
time = datetime.now()
dt_string = time.strftime("%d/%m/%Y %H:%M:%S")
print("Date and Time:", dt_string)	
print()
print("Please enter the price of each individual item in the designated spot.")
print("Enter '0' when you are done.")
print()

num=float(input("Enter the price of the next item($):"))
subtotal=0.0
tax=0.0
total=0.0
count=0

while(num!=0 and num>0):
    subtotal=subtotal+num
    tax=round((0.13*subtotal),2)
    total=round((subtotal+tax),2)
    count=count+1
    num=float(input("Enter the price of the next item($):"))
print()
print("Subtotal:$",subtotal)
print("Tax(13%):$",tax)
print("Total:$",total)
print("Items purchased:",count)
print("Thank you for your purchase!")
print("Please come again!")
