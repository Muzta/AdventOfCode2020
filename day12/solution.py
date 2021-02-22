'''
Created on 20 feb. 2021

@author: javyn
'''
import pathlib

file = str(pathlib.Path(__file__).parent) + "\input.txt"

def partOne(index, coordinates, facing):
    if index == len(lines): return abs(coordinates[0]) + abs(coordinates[1])  # if no more lines, return manhattan distance 

    instruction = lines[index]
    action = instruction[0]
    value = int(instruction[1:])
    nIndex = index + 1

    if action == "N": return partOne(nIndex, [coordinates[0], coordinates[1] + value], facing)
    elif action == "S": return partOne(nIndex, [coordinates[0], coordinates[1] - value], facing)
    elif action == "E": return partOne(nIndex, [coordinates[0] + value, coordinates[1]], facing)
    elif action == "W": return partOne(nIndex, [coordinates[0] - value, coordinates[1]], facing)
    elif action == "F": 
        vectorForward = [x * value for x in facing]
        return partOne(nIndex, [coordinates[0] + vectorForward[0], coordinates[1] + vectorForward[1]], facing)
    else:
        rotations = int(value/90)  # number of rotations of 90º in that direction
        if rotations == 2: return partOne(nIndex, coordinates, [x * (-1) for x in facing]) # it rotates 180º

        if action == "L": nFacing = [- facing[1], facing[0]]
        elif action == "R": nFacing = [facing[1], - facing[0]]

        if rotations == 3: nFacing = [x * (-1) for x in nFacing]    # rotation of 270º is the negative of 90º
        return partOne(nIndex, coordinates, nFacing)

with open(file) as doc:
    lines = doc.readlines()
lines = [x.strip() for x in lines]

# Part one
print("Distance for first part of the problem is " + str(partOne(0, [0, 0], [1, 0])))
