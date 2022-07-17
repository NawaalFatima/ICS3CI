#Nawaal Fatima
# Nov 12, 2019
#h002.py
#Use user-imput names and output in reverse order.

names=[]
for x in range (5):
    x=input("Please enter a name:")
    names.append(x)
    
names.reverse()

for i in range(5):
    print(names[i])
    
