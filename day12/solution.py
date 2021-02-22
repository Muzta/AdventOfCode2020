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

        elif action == "L": # vector if it rotates 90º to the left
            if facing[0] != 0: rotate = [x * facing[0] for x in [-1, 1]] # it is in x axis
            else: rotate = [x * facing[1] for x in [-1, -1]]   # it is in y axis

        elif action == "R": # vector if it rotates 90º to the right
            if facing[0] != 0: rotate = [x * facing[0] for x in [-1, -1]] # is is in x axis
            else: rotate = [x * facing[1] for x in [1, -1]] # is is in y axis

        if rotations == 1: return partOne(nIndex, coordinates, [facing[0] + rotate[0], facing[1] + rotate[1]])
        else: return partOne(nIndex, coordinates, [- (facing[0] + rotate[0]), - (facing[1] + rotate[1])])    # rotation of 270º is the negative of 90º


with open(file) as doc:
    lines = doc.readlines()
lines = [x.strip() for x in lines]

# Part one
print("Distance for first part of the problem is " + str(partOne(0, [0, 0], [1, 0])))