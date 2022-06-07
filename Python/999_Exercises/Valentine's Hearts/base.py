peoplelist =["Mom", "cat", "sister", "friend"]
complist = [" is smart!", " has a great personality!", " rocks!"]

import random
peoplenum = random.randrange(0, len(peoplelist))
compnum = random.randrange(0, len(complist))

print(peoplelist[peoplenum] + complist[compnum])