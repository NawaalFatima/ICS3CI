#Nawaal Fatima
# Nov 12, 2019
#h001.py
# Create a list of 5 numbers, sort then print smallest one on screen

import random

int=[]
for x in range (5):
    x=random.randint(1,1000)
    int.append(x)
print("The list is:",int) 
int.sort()
print("The smallest number is:",int[0])
