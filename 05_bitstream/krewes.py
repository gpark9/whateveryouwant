'''
Gitae Park & Gabriel Thompson
SoftDev
K05 -- krewes/Making a random generator to return the name of a student given a file krewes.txt
2022-09-29
.3 hrs
OP Summary for randomdevo()
1) Read the txt file
2) Split the txt at all "@@@" into lists of all individuals
3) Iterated through list and split at "$$$" into lists of pd, devos, ducky
4) Assigned Devos as key in dictionary devo and list of pd and ducky as value of each key
5) Randomly chose a key and printed devos name, pd, and ducky name

Q/C/C
How do I make a dictionary within a dictionary?

DISCO
.split method, how to assign keys and values in a dictionary
'''


import random
f = open('krewes.txt', 'r')
content = f.read()

each = content.split("@@@")

devos = {}

for x in each :
    individual = x.split("$$$")
    devos[individual[1]] = [individual[0], individual[2]]
    
rand = random.choice(list(devos.keys()))


print(rand + " in pd " + devos[rand][0] + " with ducky " + devos[rand][1])
