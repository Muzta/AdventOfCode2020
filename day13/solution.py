'''
Created on 21 feb. 2021

@author: muzta
'''
import pathlib

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


with open(file) as doc:
    lines = doc.readlines()
earliestDepart = int(lines[0].strip())
busList = [int(b) for b in (lines[1].split(",")) if b != "x"]    # dont include "x" in the list

# Part One
print("Time to wait in first part is " + str(partOne()))