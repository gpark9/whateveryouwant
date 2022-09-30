import random

f = open('occupations.csv', 'r')
content = f.read()

split = content.split("\n")

dict = {}

for x in split:
    if x[0] == "\"" :
        job = x.split("\",")
    else :
        job = x.split(",")
    dict[job[0]] = job[1]
    
total = dict["Total"]

dict.pop("Job Class")
dict.pop("Total")

r = random.random() * 99.8

sum = 0
for x in list(dict.keys()):
     sum += float(dict[x])
     if r < sum :
        print(x)
        break

