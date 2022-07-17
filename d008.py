#Nawaal Fatima
#Oct 4, 2019
#d008.py
#Input numbers from user, print sum of positive numbers when negative num is entered.

sum=0
num=int(input("Please enter a number. Enter a negative number when you want to quit."))
while(num>=0):
    sum=sum+num
    num=int(input("Please enter a number:"))
   
print("The sum is",sum,".")
