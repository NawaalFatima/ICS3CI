#Nawaal Fatima
#Oct 8, 2019
#d011.py
#Input PIN from user until '2357' is entered

num=int(input("Please enter the PIN number:"))

while(num!=2357):
    print("Invalid PIN number.")
    num=int(input("Please enter the PIN number:"))

print("APPROVED")
