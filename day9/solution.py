'''
Created on 2 feb. 2021

@author: javyn
'''
import pathlib

file = str(pathlib.Path(__file__).parent) + "\input.txt"
preamble = 25

def partOne(index, lines, listPreambles):
    currentNumber = lines[index]
    canSum = False
    for n in listPreambles:
        checkList = listPreambles.copy()    # Aux list to not sum a previous number by itself
        checkList.remove(n)
        for m in checkList:
            if n + m == currentNumber:   # If the two numbers are found, stop
                canSum = True
                break
        if canSum : break    
    
    if canSum == False: return index
    
    newListPreambles = (listPreambles[1:])  # New list without the first number
    newListPreambles.append(currentNumber)   # Add the current number to the preambles
    return partOne(index+1, lines, newListPreambles)


def partTwo(index, lines, lowerX, lowerY):
    finalIndex = len(lines) - 1 # The target number to be the result of the sum
    for x in range(index, finalIndex):
        for y in range(index + 1, finalIndex):
            if sum(lines[x:y+1]) == lines[finalIndex]:
                if (y - x) < (lowerY - lowerX): # If this range is smaller, take it
                    lowerY = y
                    lowerX = x
        return partTwo(index + 1, lines, lowerX, lowerY)
    
    #once the range of number is found
    greatest = max(lines[lowerX:lowerY + 1])
    lowest = min(lines[lowerX:lowerY + 1])
    return greatest + lowest
    

with open(file) as doc:
    lines = doc.readlines()
lines = [int(x.strip()) for x in lines]

# Part one
listPreambles = lines[:preamble]
index = partOne(preamble, lines, listPreambles)
print("The number which can't be obtained with its preambles is " + str(lines[index]))

# Part two
sumRange = partTwo(0, lines[:index + 1], 0, len(lines))
print("The sum resulted in part two is " + str(sumRange))