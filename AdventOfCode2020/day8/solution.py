'''
Created on 14 dic. 2020

@author: muzta
'''
file = "input.txt"

def iterateInstructions(index, instructions, accumulator, listIndex):
    ins = instructions[index]   # current instruction
    action = ins.split(" ")[0]  # kind of action
    number = int(ins.split(" ")[1])  # value of action
    if index in listIndex : return accumulator   # if it has already passed by the index, return the acumulator
    listIndex.append(index)
    if action == "acc" : return iterateInstructions(index + 1, instructions, accumulator + number, listIndex)
    elif action == "nop" : return iterateInstructions(index + 1, instructions, accumulator, listIndex)
    elif action == "jmp" : return iterateInstructions(index + number, instructions, accumulator, listIndex)


def switch(value):
    return "nop" if value == "jmp" else "jmp"

def findInstructionToChange(index, instructions, accumulator, listIndex, accIndexes):
    ins = instructions[index]   # current instruction
    action = ins.split(" ")[0]  # kind of action
    number = int(ins.split(" ")[1])  # value of action
    if index == len(instructions) : return accumulator
    
    if index in listIndex : 
        nAccIndexes = len(accIndexes)   # number of accumulator instruction indexes since the last nop/jmp
        listIndex = listIndex[:-nAccIndexes]
        for x in accIndexes:
            accumulator -= int(instructions[x].split()[1])
        backIndex = listIndex[len(listIndex) - 1]   # index of the last nop/jmp instruction
        if "nop" in instructions[backIndex] : instructions[backIndex].replace("nop", "jmp")
        else : instructions[backIndex].replace("jmp", "nop")
        
        return findInstructionToChange(backIndex, instructions, accumulator, listIndex, [])   # if it has already passed by the index, return the acumulator
    
    listIndex.append(index)
    
    if action == "acc" : 
        accIndexes.append(index)
        return findInstructionToChange(index + 1, instructions, accumulator + number, listIndex, accIndexes)
    
    elif action == "nop" : return findInstructionToChange(index + 1, instructions, accumulator, listIndex, accIndexes)
    
    elif action == "jmp" : return findInstructionToChange(index + number, instructions, accumulator, listIndex, accIndexes)
    

with open(file) as doc:
    instructions = doc.readlines()
instructions = [x.strip() for x in instructions]

# Part one
acc = iterateInstructions(0, instructions, 0, [])
print("The value of the accumulator before the second loop start is " + str(acc))


l = [1, 2, 3, 4, 5]
print(l)
print(l[:-2])
# Part two
# acc2 = findInstructionToChange(0, instructions, 0, [], [])
# print("The second excercise is " + str(acc2))