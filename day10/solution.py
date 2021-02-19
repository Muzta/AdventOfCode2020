'''
Created on 3 feb. 2021

@author: javyn
'''
import pathlib

file = str(pathlib.Path(__file__).parent) + "\input.txt"

def partOne(currentNumber, lines, oneJolt, threeJolts):
    if currentNumber < max(lines):
        if currentNumber + 1 in lines: 
            oneJolt+=1
            newNumber = currentNumber + 1
        elif currentNumber + 2 in lines: newNumber = currentNumber + 2
        elif currentNumber + 3 in lines:
            threeJolts+=1
            newNumber = currentNumber + 3
            
        return partOne(newNumber, lines, oneJolt, threeJolts)
    
    return oneJolt*(threeJolts) # The built-in adapter is 3 higher
        
def partTwo(lines):
    sol = {0:1}
    for line in lines[1:]:  # Except the 0
        sol[line] = 0
        if line - 1 in sol: sol[line]+=sol[line-1]  # Possibilities of reaching the number
        if line - 2 in sol: sol[line]+=sol[line-2]
        if line - 3 in sol: sol[line]+=sol[line-3]

    return sol[max(lines)]
    

with open(file) as doc:
    lines = doc.readlines()
lines = [int(x.strip()) for x in lines]

#Part one
lines.append(max(lines) + 3)    # The max jolt
lines.append(0) # The start
number = partOne(0, lines, 0, 0)
print("The multiplication of 1Jolt differences by 3Jolts differences is " + str(number))

#Part two
print("The number of distinct ways to arrange the adapters is " + str(partTwo(sorted(lines))))