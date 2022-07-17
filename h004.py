#Nawaal Fatima
# Nov 12, 2019
#h004.py
#generate a list of 100 rand ints between 1-20. Then print smallest&largest num

import random
num=[]
for x in range(100):
    x=random.randint(1,1000)
    num.append(x)
num.sort()
print("The smallest number generated was:",num[0])
print("The largest number generated was:",num[99])
    
