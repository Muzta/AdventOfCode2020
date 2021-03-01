'''
Created on 24 feb. 2021

@author: muzta
'''
import pathlib

file = str(pathlib.Path(__file__).parent) + "\input.txt"

def partOne():
    dictionary = {}

    for l in lines:
        if "mask" in l: 
            mask = l.split("=")[1].strip()  # if a new mask appear, take it and go next line
            continue
        
        line = l.split("=")
        value = int(line[1].strip())
        value = bin(value)
        start, end = l.index("["), l.index("]") # indexes for the substring
        memory = l[start + 1:end]   # memory address
        value = applyMask(value[2:], mask)    # apply the mask to the bin number but the two first characters '0b'
        dictionary[memory] = value  # overwrite the value in that memory

    sumMemories = sum(dictionary.values())
    print(sumMemories)


def applyMask(number, mask):
    rNumber = list(str(number)[::-1])  # reverse the number
    rMask = list(mask[::-1])  # reverse the mask
    
    for x in range(len(rMask)):
        if rMask[x] != 'X': continue    # vaule of bits in the mask is the most important
        else:
            try: rMask[x] = rNumber[x] 
            except IndexError: rMask[x] = '0'   # if x is not index of the number, write 0

    rMask = "".join([elem for elem in rMask])  # convert the list to a string
    rMask = rMask[::-1] # reverse the result to get the bin number
    decimalValue = int(rMask, 2)    # convert to decimal number
    
    return decimalValue
        

with open(file) as doc:
    lines = doc.readlines()

# Part One
partOne()
# print("Time to wait in first part is " + str(partOne()))

# partTwo()
# print("Earliest timestamp for second part is " + str(partTwo()))