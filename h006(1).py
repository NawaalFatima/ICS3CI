#Nawaal Fatima
# Nov 12, 2019
#h006.py
#Use user-inputted numbers to find the median mark. Stop when '999' is entered

import statistics
list=[]
mark=float(input("Please enter a mark. Enter '999' to quit:"))
while(mark!=999):
    list.append(mark)
    mark=float(input("Please enter a mark. Enter '999' to quit:"))
    
list.sort()
length=len(list)
median=statistics.median(list) #googled it
print("The median of the marks is:",median)

