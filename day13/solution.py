'''
Created on 21 feb. 2021

@author: muzta
'''
import pathlib
from functools import reduce

file = str(pathlib.Path(__file__).parent) + "\input.txt"

def partOne():
    timeToWait = 0
    busId = 0
    for x in busList:
        diff = (x * (int(earliestDepart/x) + 1)) - earliestDepart
        if timeToWait == 0 or timeToWait > diff: 
            timeToWait = diff
            busId = x
    return timeToWait * busId

def partTwo():
    departList = [0]    # list of minutes after "t" buses will depart
    for b in allBusesList[1:]:
        if b != "x": departList.append(int(allBusesList.index(b)))

    nList = []  # list of offsets
    for i in range(len(departList)):
        nList.append(busList[i] - departList[i])

    return chinese_remainder(busList, nList)

# Chinese remainder theorem, the code is copied from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
 
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

with open(file) as doc:
    lines = doc.readlines()
earliestDepart = int(lines[0].strip())
busList = [int(b) for b in (lines[1].split(",")) if b != "x"]    # dont include "x" in the list
allBusesList = [b for b in (lines[1].split(","))]

# Part One
print("Time to wait in first part is " + str(partOne()))

# partTwo()
print("Earliest timestamp for second part is " + str(partTwo()))