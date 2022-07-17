#Nawaal Fatima
# Nov 12, 2019
#h005.py
#Use 20 user-inputted numbers to find the median mark

import statistics

list=[]
for mark in range(20):
    mark=int(input("Please enter a mark between 0-100:"))
    list.append(mark)
list.sort()
median=statistics.median(list)
print("The median of the marks is:",median)

