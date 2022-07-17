#Nawaal Fatima
#Oct 8, 2019
#d010.py
#Input numbers from user and print smallest positive number entered when negative number is entered.

num=int(input("Please enter a number. Enter a NEGATIVE number when you want to quit:"))
smallest=100
while(num>=0):
    if(smallest>=num):
        smallest=num
    num=int(input("Please enter a number:"))
            
print("The smallest number entered was",smallest,".")
