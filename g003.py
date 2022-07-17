#Nawaal Fatima
#Oct 24, 2019
#g003.py
#Identify pattern in set of strings (both are from user) & then print its index
#Print 'Goodbye!' when 'exit' is entered

pattern=input("Please enter a pattern:")
word=input("Please enter a word(or exit to quit):")

while(word!="exit" and word!="Exit" and word!="EXIT"):
    num=word.find(pattern)
    print("The index is",num,".")
    word=input("Please enter a word(or exit to quit):")
print("Goodbye!")

