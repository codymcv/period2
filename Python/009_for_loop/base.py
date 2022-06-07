line=int(input("Enter line legth: "))
hv=input("Do you want horizontal or vertical (h or v): ")
if hv=="h":
    for x in range(0,line):
        print("*", end="")
elif hv=="v":
    for y in range(0,line):
        print("*")
elif hv=="horizontal":
    for x in range(0,line):
        print("*", end="")
elif hv=="vertical":
    for y in range(0,line):
        print("*")
else:
    print("you did not choose horizontal or vertical")