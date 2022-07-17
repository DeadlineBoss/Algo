from socket import if_nameindex
from statistics import mode

strng = str(input("Enter String: "))

liststr = list(strng)
dictnry = {"A":0}

for i in liststr:
    if i in dictnry.keys():
        dictnry[i] += 1
    else:
        dictnry[i] = 1

sameNot = all(ele == dictnry for ele in dictnry.values())
x = -1
fix = {1:0}
dictFix = {0:0}
t = 1
b = 0
c = 0

if sameNot == False:
    for i in dictnry.values():
        if i != max(dictnry.values()):
            x += 1
            dictFix[x] = i

    for i in dictFix:
        fix[i] += 1
        if fix[i] == 2:
            keys = [k for k, v in dictnry.items() if v == i]
                        

    sameNot = all(ele == dictnry for ele in dictnry.values())

print(dictnry)