#Nawaal Fatima
#Sept 26,2019
#MultipleChoiceQuiz.py
#Generate a 10 question quiz for user and calculate(then print)score after every question.

print("Welcome to the General Knowledge Quiz!")
print("You will be asked 10 questions. Enter your answer in the deignated spot.")
print("Enter 'a','b',or 'c' as your answer. This quiz is not case-sensitive!")
print("Goodluck!")
print()

score=0
print("Q1. Which country has the capital,Berlin?")
print("A)Belgium")
print("B)Netherlands")
print("C)Germany")
answer1=input("Enter your choice:")
if(answer1=="C" or answer1=="c"):
    print("Correct!")
    score=score+1
else:
    print("Incorrect!")
print("Your score so far is",score,"out of 1")

print()

print("Q2. In what year did WW2 end?")
print("A)1939")
print("B)1943")
print("C)1945")
answer2=input("Enter your choice:")
if(answer2=="C" or answer2=="c"):
   print("Correct!")
   score=score+1
else:
    print("Incorrect!")
print("Your score so far is",score,"out of 2")

print()

print("Q3. Does gravity exist on the moon?")
print("A)Yes it does, silly!")
print("B)No, science says so.")
print("C)Maybe...Tidal waves,am I right?")
answer3=input("Enter your choice:")
if(answer3=="A" or answer3=="a"):
    print("Correct!")
    score=score+1
else:
    print("Incorrect!")
print("Your score so far is",score,"out of 3")

print()

print("Q4. If you want to make purple paint, which colors do you mix together?")
print("A)Red and Yellow")
print("B)Blue and Red")
print("C)Blue and Orange")
answer4=input("Enter your choice:")
if(answer4=="B" or answer4=="b"):
    print("Correct!")
    score=score+1
else:
    print("Incorrect!")
print("Your score so far is",score,"out of 4")

print()

print("Q5. Which of the following listed countries gifted the Statue Of Liberty to U.S.A?")
print("A)The U.K")
print("B)France")
print("C)Italy")
answer5=input("Enter your choice:")
if(answer5=="B" or answer5=="b"):
    print("Correct!")
    score=score+1
else:
    print("Incorrect!")
print("Your score so far is",score,"out of 5")

print()

print("Q6. Which of the following is the longest river in Canada?")
print("A)Yukon River")
print("B)Columbia River")
print("C)Amazon River")
answer6=input("Enter your choice:")
if(answer6=="A" or answer6=="a"):
    print("Correct!")
    score=score+1
else:
    print("Incorrect!")
print("Your score so far is",score,"out of 6")

print()

print("Q7. Which of these eras came first?")
print("A)Bronze Age")
print("B)Stone Age")
print("C)Iron Age")
answer7=input("Enter yuor choice:")
if(answer7=="B" or answer7=="b"):
    print("Correct!")
    score=score+1
else:
    print("Incorrect!")
print("Your score so far is",score,"out of 7")

print()

print("Q8. How many rings are on the Olympic Flag?")
print("A)5")
print("B)4")
print("C)6")
answer8=input("Enter your choice:")
if(answer8=="A" or answer8=="a"):
    print("Correct!")
    score=score+1
else:
    print("Incorrect!")
print("Your score so far is",score,"out of 8")

print()

print("Q9. Who wrote the Harry Potter Series?")
print("A)Rick Riordan")
print("B)J.K. Rowling")
print("C)Lev Grossman")
answer9=input("Enter your choice:")
if(answer9=="B" or answer9=="b"):
    print("Correct!")
    score=score+1
else:
    print("Incorrect!")
print("Your score so far is",score,"out of 9")

print()

print("Q10. If train A goes from one point to another at 4 o'clock and train B arrives at the same time")
print("How important is it to wash your hands before eating?")
print("A)Meh.Depends really...")
print("B)It is extremely important!")
print("C)Washing hands is for babies!!!")
answer10=input("Enter your choice:")
if(answer10=="B" or answer10=="b"):
    print("Correct!")
    score=score+1
else:
    print("Incorrect!")
print("Your score so far is",score,"out of 10")

print()

if(score>=0 and score<5):
    print("You tried...I guess?")
elif(score>=5 and score<=9):
     print("Wow! Good job!")
else:
     print("YOU ARE A GENIUS!!!")

print()
print("Goodbye!")

   



