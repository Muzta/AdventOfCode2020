'''
Created on 24 feb. 2021

@author: muzta
'''
import pathlib
import itertools

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
    return sumMemories

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
        

def partTwo():
    dictionary = {}

    for l in lines:
        if "mask" in l: 
            mask = l.split("=")[1].strip()  # if a new mask appear, take it and go next line
            continue
        
        line = l.split("=")
        value = int(line[1].strip())
        start, end = l.index("["), l.index("]") # indexes for the substring
        memory = l[start + 1:end]   # memory address
        memory = bin(int(memory))
        lsAddress = applyMaskSecondPart(memory[2:], mask)    # apply the mask to the bin number but the two first characters '0b' and get the lisft of affected addresses
        for a in lsAddress: dictionary[a] = value  # overwrite the value in that memory

    sumMemories = sum(dictionary.values())
    return sumMemories

def applyMaskSecondPart(number, mask):
    rNumber = list(str(number)[::-1])  # reverse the number
    rMask = list(mask[::-1])  # reverse the mask
    listAddresses = []  # list of addresses it will overwrite
    for x in range(len(rMask) - len(rNumber)): rNumber.append("0")  # fill the binary number with 0s
    
    for x in range(len(rMask)): # floating number address
        if rMask[x] == "0": continue
        elif rMask[x] == "1": rNumber[x] = "1"
        elif rMask[x] == "X": rNumber[x] = "X"

    listFloating = []   # list of indexes of Xs for that number
    for x in range(len(rNumber)): 
        if rNumber[x] == "X": listFloating.append(x)

    possibilities = list(itertools.product(["0", "1"], repeat=len(listFloating)))   # list of all binary posibilities for Xs in that number

    for p in possibilities:
        address = rNumber.copy()
        for x in range(len(p)): address[listFloating[x]] = p[x] # update the floating in 'x' index with bit in 'x' position in possibility p
        
        listAddresses.append(address)

    listAddresses = ["".join([elem for elem in address]) for address in listAddresses]  # convert all addresses to a string
    listAddresses = [d[::-1] for d in listAddresses]    # reverse all address strings
    listAddresses = [int(d, 2) for d in listAddresses]  # convert all addresses to int

    return listAddresses

with open(file) as doc:
    lines = doc.readlines()

# Part One
print("The sum of values of all memories is " + str(partOne()))

# partTwo()
print("The sum of values of all memories is " + str(partTwo()))