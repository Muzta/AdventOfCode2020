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

#Same function but with some changes
def iterateInstructionsTwo(index, instructions, accumulator, listIndex):
    ins = instructions[index]   # current instruction
    action = ins.split(" ")[0]  # kind of action
    number = int(ins.split(" ")[1])  # value of action
    lastAcc = number if "acc" in action else 0  # if the last instruction is acc, we have to sum it
    if index == (len(instructions) - 1) : return accumulator + lastAcc  # if the index is in the last position, it finishes
    
    if index not in listIndex:
        listIndex.append(index)
        if action == "acc" : return iterateInstructionsTwo(index + 1, instructions, accumulator + number, listIndex)
        elif action == "nop" : return iterateInstructionsTwo(index + 1, instructions, accumulator, listIndex)
        elif action == "jmp" : return iterateInstructionsTwo(index + number, instructions, accumulator, listIndex)
        
def switch(value):
    if "jmp" in value:
        value = value.replace("jmp", "nop")
    else:
        value = value.replace("nop", "jmp")
    return value

def findInstructionToChange(instructions):
    for i in range(len(instructions)):
        if ("nop" in instructions[i] or "jmp" in instructions[i]) and "nop +0" not in instructions[i]:
            instructions[i] = switch(instructions[i])
            acc = iterateInstructionsTwo(0, instructions, 0, [])
            if acc is not None: return acc
            else: instructions[i] = switch(instructions[i])
    
    
with open(file) as doc:
    instructions = doc.readlines()
instructions = [x.strip() for x in instructions]

# Part one
acc = iterateInstructions(0, instructions, 0, [])
print("The value of the accumulator before the second loop start is " + str(acc))


# Part two
acc2 = findInstructionToChange(instructions)
print("The accumulator after the program terminates is " + str(acc2))