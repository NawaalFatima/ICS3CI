#Nawaal Fatima
#Oct 24, 2019
#g004.py
# Print 'Pattern not found' when a pattern is not found in a string
#Both pattern and string are user-input

pattern=input("Please enter a pattern:")
word=input("Please enter a word(or exit to quit):")

while(word!="exit" and word!="Exit" and word!="EXIT"):
    num=word.find(pattern)
    if(num<0):
        print("Pattern not found.")
    else:
        print("The index is",num,".")
    word=input("Please enter a word(or exit to quit):")
print("Goodbye!")
