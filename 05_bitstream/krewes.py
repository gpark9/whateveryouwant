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
