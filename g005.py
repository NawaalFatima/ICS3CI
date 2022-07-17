#Nawaal Fatima
#Oct 24, 2019
#g005.py
# Print Yes when a pattern is found in a string & vice versa
#Also, rint the number of words it was found in(Both pattern and string are user-input)

pattern=input("Please enter a pattern:")
word=input("Please enter a word(or exit to quit):")
count=0

while(word!="exit" and word!="Exit" and word!="EXIT"):
    num=word.find(pattern)
    if(num<0):
        print("No.")
    else:
        print("Yes.")
        count=count+1
    word=input("Please enter a word(or exit to quit):")
if (count>1):
    print("The pattern was found in",count,"words.")
else:
    print("The pattern was found in",count,"word.")
print("Goodbye!")
