a=int(input("How many items are you buying?: "))

total=0
for x in range (0,a):
    item= input("What item are you buying?: ")
    price= float(input("How much does it cost?: $"))
    total=total+price
    print("____________________")
print("Your total is " + str(total))
