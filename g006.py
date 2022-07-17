#Nawaal Fatima
#Oct 24, 2019
#g006.py
#Print the 2nd&3rd characters of a string entered by a user.
#Print 'Goodbye!' when 'exit' is entered

word=input("Please enter a word:")
while(word!='exit' and word!='Exit' and word!="EXIT"):
    char=word[1:3]
    print(char)
    word=input("Please enter a word:")
print("Goodbye!")
