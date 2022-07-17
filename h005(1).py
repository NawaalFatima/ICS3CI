#Nawaal Fatima
# Nov 12, 2019
#h005.py
#Use 20 user-inputted numbers to find the median mark

count=20
list=[]
for mark in range(20):
    mark=int(input("Please enter a mark between 0-100:"))
    count=count-1
    print("Enter",count,"more marks.")
    list.append(mark)
    
list.sort()
length=len(list)
num= int(length/2) # finding middle number
num1=list[num-1] # slices start from 0
num2=list[num] # slices start from 0
median=(0.5*(num1+num2))
print()
print("The median of the marks is:",median)

