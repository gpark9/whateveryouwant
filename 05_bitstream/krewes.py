'''
GAGI - Gitae Park & Gabriel Thompson
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
.split method
how to assign keys and values in a dictionary
'''


import random

opened_file = open('krewes.txt', 'r')
content = opened_file.read()

devos_list = content.split("@@@")
devos_dict = {}

for devo in devos_list:
    pd_name_ducky = devo.split("$$$")
    pd = pd_name_ducky[0]
    name = pd_name_ducky[1]
    ducky = pd_name_ducky[2]

    devos_dict[name] = [pd, ducky]
    
random_devo = random.choice(list(devos_dict.keys()))


print(random_devo + \
      " in pd " + \
      devos_dict[random_devo][0] + \
      " with ducky " + \
      devos_dict[random_devo][1])

