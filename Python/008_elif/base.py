one=int(input("Please enter a number: "))
op=str(input("Please enter an operation (+,-,*,/): "))
two=int(input("Please enter a second number: "))

add=str(one+two)
sub=str(one-two)
mult=str(one*two)
dev=str(one/two)

if op == "+":
    print(str(one) + "+" + str(two) + "=" + add)
elif op == "-":
    print(str(one) + "-" + str(two) + "=" + sub)
elif op == "*":
    print(str(one) + "*" + str(two) + "=" + mult)
elif op == "/":
    print(str(one) + "/" + str(two) + "=" + dev)
else:
    print("Your operation is not noticable, try with a new one")