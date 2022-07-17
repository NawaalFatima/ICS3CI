#Nawaal Fatima
#Oct 28, 2019
#g007.py
#Replace 'r'&'R" from user input line and print the rest of the sentence
#Print 'Goodbye!' when 'exit' is input

line=input("Enter 'exit' to quit.Please enter a line:")
while(line!="exit" and line!="Exit" and line!="EXIT"):
    new_line=line.replace("r","")
    new_line=new_line.replace("R","")
    print(new_line)
    line=input("Enter 'exit' to quit.Please enter a line:")
print("Goodbye!")
