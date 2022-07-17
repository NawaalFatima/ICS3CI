#Nawaal Fatima
#Sept 30, 2019
#TriangleTimes.py
#Use input of 3 angles and determine(then print) the type of triangle

angle1=int(input())
angle2=int(input())
angle3=int(input())

sum=angle1+angle2+angle3

if(sum!=180):
    print("Error")
else:
    if(angle1==angle2==angle3==60):
        print("Equilateral")
    elif(angle1==angle2 or angle1==angle3 or angle2==angle3):
        print("Isosceles")
    else:
        print("Scalene")

