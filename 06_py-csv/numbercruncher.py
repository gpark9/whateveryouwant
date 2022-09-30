'''
GAGI - Gitae Park & Gabriel Thompson
SoftDev
K06 -- StI/O: Divine your Destiny!
2022-09-30
.3 hrs
OP Summary for randomdevo()
1) Read the csv file
2) Split the txt at all "\n" into a list of occupation and percentage
3) Create a dictionary
4) Iterate through the list and split at "," for occupation names without commas and "\"," with occupation names with commas into a list occupation and percentage
5) assign occupation as key and percentage as value in dictionary
6) save total percentage, pop the first key and last key
7) produce a random float between 0 and total
8) start a running sum
9) go through each key and value, add the value to the running sum, and check if the running sum is larger than the random float
10) if larger, than print occupation
Q/C/C
Is there a better way to manage the commas insied the quotation marks?
DISCO
.pop()
can interate through keys ofd dictionary just by for x in dict
'''


import random

f = open('occupations.csv', 'r')
content = f.read()

split = content.split("\n")

dict = {}

for x in split:
    if x == "" :
        continue
    if x[0] == "\"" :
        job = x.split("\",")
    else :
        job = x.split(",")
    dict[job[0]] = job[1]
    
total = dict["Total"]

dict.pop("Job Class")
dict.pop("Total")

r = random.random() * float(total)

sum = 0
for x in dict:
     sum += float(dict[x])
     if r < sum :
        if x[0] == "\"" :
            x = x[1:]
        print(x)
        break





