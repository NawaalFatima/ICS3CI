#Nawaal Fatima
#Oct 4, 2019
#d006.py
#Input words from user and say 'goodbye' when 'exit' is entered. Keep score of words entered.

count=0
word=input("Please enter a word. Enter 'exit' when you want to quit:")
while(word!='exit'):
    word=input("Please enter a word. Enter 'exit' when you want to quit:")
    count=count+1
print("You entered",count,"words.")
