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
import time
t0 = time.time()

opened_file = open('occupations.csv', 'r')
content = opened_file.read()

lines = content.split("\n")

percentages = {}

for line in lines:
    if line == "" :
        continue
    if line[0] == "\"" :
        job_percent = line.split("\",")
    else:
        job_percent = line.split(",")

    job = job_percent[0]
    percent = job_percent[1]
    percentages[job] = percent
    
total = percentages["Total"]

percentages.pop("Job Class")
percentages.pop("Total")

r = random.random() * float(total)

sum = 0
for key in percentages:
     sum += float(percentages[key])
     if r < sum:
        if key[0] == "\"" :
            key = key[1:]
        print(key)
        break

print(time.time() - t0)


