x = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"

c=0
for i in range(0,len(x)):
    y=x[i:i+5]
    if y=="whale":
        c=c+1
print("whale is said " + str(c) + " times")


print("-------")


with open('moby.txt') as f:
    for line in f:
        x = line.strip()
        for i in range(0,len(x)):
            y=x[i:i+5]
            if y=="whale":
                c=c+1
print("whale is said " + str(c) + " times")

f.close()
