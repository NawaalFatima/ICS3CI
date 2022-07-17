#Nawaal Fatima
#Sept 26,2019
#c005.py
#input number from user(1<=x<=100) and ask user to guess the number.
#Then print number and tell how close they were.

import random
num = random.randint(1,100)

print("I have chosen a number between 1 and 100.Try to guess it!")
guess1=int(input("Guess #1:"))
guess2=int(input("Guess #2:"))

diff1=abs(guess1-num)
diff2=abs(guess2-num)

print("The number was",num)

if(diff1<diff2):
    print("Your first guess was closer")
else:
    print("Your second guess was closer")

