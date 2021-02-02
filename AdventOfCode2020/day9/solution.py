'''
Created on 2 feb. 2021

@author: javyn
'''
file = "input.txt"
preamble = 25

def ex1(index, lines, listPreambles):
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
    
    if canSum == False: return lines[index]
    
    newListPreambles = (listPreambles[1:])  # New list without the first number
    newListPreambles.append(currentNumber)   # Add the current number to the preambles
    return ex1(index+1, lines, newListPreambles)

with open(file) as doc:
    lines = doc.readlines()
lines = [int(x.strip()) for x in lines]

# Part one
listPreambles = lines[:preamble]
print("The number which can't be obtained with its preambles is " + str(ex1(preamble, lines, listPreambles)))