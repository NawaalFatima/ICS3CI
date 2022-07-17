#Nawaal Fatima
#Oct 16,2019
#GuessMyNumberGame.py
#Make a game that asks user to guess the computer's number(random)
#Print appropriate message and ask the user to guess again if incorrect guess

import random
num = random.randint(1,100)
count=0

print("Welcome to 'Guess My Number' Game!")
print("Try to guess the number the computer is thinking of.")
print()
guess=int(input("Please enter a number between 1 and 100:"))

while(num!=guess):
    count=count+1
    if(num>guess):
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess=int(input("Please enter a number between 1 and 100:"))
    
print()
print("That is correct!")
print("The number was",num)
print("It took you",count,"guesses.")
