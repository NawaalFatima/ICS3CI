#Nawaal Fatima
#Oct 30, 2019
#WheelofFortune.py
#Build the Wheel Of Fortune Game from Hangman

import random

def game():
    print()
    print ("Time to play Wheel of Fortune!!!")
    print()
    print("Please turn on the CAPS LOCK for this game.")
    print("Failure to do so will result in error.")
    print()
    guesses = "  STVY&.,"   
    phrases = ["TO  BE  OR  NOT  TO  BE  THAT  IS  THE  QUESTION.","I  LIKE  TO  CODE  ON  MY  COMPUTER.","DUNGEONS  &  DRAGONS.","SPEECH  IS  SILVER  ,BUT  SILENCE  IS  GOLD.","ALL  THAT  GLITTERS  IS  NOT  GOLD"]
    secret=random.choice(phrases)
    total=0
    count=0
    amount=0
    missed = 1
    num=0
    loop=0

    while (missed!=0):    
        missed = 0
    
    
        for letter in secret:           
            if (letter in guesses):     
                print (letter, end="")
            else:
                print ("_", end="")     
                missed = missed + 1     
        print("")

        if (missed == 0):
            print()
            print ("You win!!")
            print("You get to take $",total,"home! Congratulations!!!")
            restart = input("Would you like to play again? Please enter '1' for YES or '2' for NO: ")
            break                       

    

    
        money=[2500,600,700,650,500,550,800,900,"BANKRUPT",1000000,100,150,200,250,300]
        win=random.choice(money)
        if(isinstance(win,int)):
            print("You win $",win,"for each letter you guess correctly this time.")
            print()
            print("Psssst...Do you want to buy all the vowels for $1500?")
            buy_vowel=input("Enter 'YES' is you want to make this purchase, else enter 'NO':")
            if (buy_vowel=="YES" and total>=1500):
                total=total-1500
                vowels =["A","E","I","O","U"]
                w=vowels[0]
                for w in vowels:
                    if w in secret:
                        guesses=guesses+w
                        loop=loop+1
                print("Thank you for your purchase!!!")
                print("They will be printed in the next round.")
                    
            elif(buy_vowel=="YES" and total<1500):
                print("Sorry, you don't have enough money. The offer still stands until the end of the game.")
            elif(buy_vowel== "NO"):
                print("Okay!The offer still stands until the end of the game.")
        else:
            print("You landed on:",win)
            print()
            print("Sorry, but you lost the game.")
            print("Your total earnings are $",total)
            print("Better luck next time!")
            print()
            restart = input("Would you like to play again? Please enter '1' for YES or '2' for NO: ")
            break
    
        guess = input("Guess a letter: ")
        guesses = guesses + guess  

        if guess not in secret:
            total=total-500
            print ("Nope!")
            print("You lost $500! You have $",total,"remaining.")
        else:
            x=secret.count(guess)
            amount=x*win
            total=total+amount
            if (amount>=0 and amount<=1000):
                print("Good for you!")
                print("You won $",amount,"this round! Congratulations!!!")
                print("Your total is $",total,".")
            elif(amount>1000 and amount<=5000):
                print("Now you're talking!")
                print("You won $",amount,"this round! Congratulations!!!")
                print("Your total is $",total,".")
            elif(amount>5000 and amount<=10000):
                print("Just remember to never doubt yourself...")
                print("You won $",amount,"this round! Congratulations!!!")
                print("Your total is $",total,".")
            elif(amount>10000):
                print("WOWIE. The fruits of patience really are sweet!")
                print("You won $",amount,"this round! Congratulations!!!")
                print("Your total is $",total,".")
        
        print()
game()

def main():
    game()
    restart = input("Would you like to play again? Please enter '1' for YES or '2' for NO: ")    
    while (restart==1):
        if restart==1:
            game()
            restart = input("Would you like to play again? Please enter '1' for YES or '2' for NO: ")
        else:
            print ("Thanks for playing!")
            break
print ("Thanks for playing!")
main()


    
