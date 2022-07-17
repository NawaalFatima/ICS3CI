#Nawaal Fatima
# Nov 12, 2019
#h006.py
#Use user-inputted numbers to find the median mark. Stop when '999' is entered


list=[]
mark=float(input("Please enter a mark. Enter '999' to quit:"))
while(mark!=999):
    list.append(mark)
    mark=float(input("Please enter a mark. Enter '999' to quit:"))
    
list.sort()
length=len(list)
if ((length%2)==0):
    num= int(length/2) # finding middle number
    num1=list[num-1] # slices start from 0
    num2=list[num] # slices start from 0
    median=(0.5*(num1+num2))
    print("The median of the marks is:",median)
else:
    middlevalue=(list[int(len(list)/2)]) # middle val is median for odd no.
    print("The median of the marks is:",middlevalue)
