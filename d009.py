#Nawaal Fatima
#Oct 8, 2019
#d009.py
#Input numbers from user, print largest of positive numbers when negative num is entered.

num=int(input("Please enter a number. Enter a NEGATIVE number when you want to quit:"))
largest=0
while(num>=0):
    if(largest<=num):
        largest=num
    num=int(input("Please enter a number:"))
            
print("The largest number was",largest,".")
        
