import random
thislist=[]
a= int(input("how many random numbers would you like?: "))
for x in range (0,a):
    thislist.append(random.randrange(1,10))
print("Your numbers are: " + str(thislist))
