#Nawaal Fatima
#Oct 24, 2019
#g002.py
#input strings from user until they enter 'exit'.
#Then, print the number of characters used.

word=input("Please enter a word(or 'exit' to quit):")
num=len(word)
sum=0

while(word!="exit" and word!="Exit" and word!="EXIT"):
    sum=sum+num
    word=input("Please enter a word(or 'exit' to quit):")
    num=len(word)


if (sum>1):
    print("You entered",sum,"characters.")
else:
    print("You entered",sum,"character.")


