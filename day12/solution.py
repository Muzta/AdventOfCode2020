'''
Created on 20 feb. 2021

@author: muzta
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

def partTwo(index, coordinates, waypoint):
    if index == len(lines): return abs(coordinates[0]) + abs(coordinates[1])  # if no more lines, return manhattan distance 

    instruction = lines[index]
    action = instruction[0]
    value = int(instruction[1:])
    nIndex = index + 1

    if action == "N": return partTwo(nIndex, coordinates, [waypoint[0], waypoint[1] + value])
    elif action == "S": return partTwo(nIndex, coordinates, [waypoint[0], waypoint[1] - value])
    elif action == "E": return partTwo(nIndex, coordinates, [waypoint[0] + value, waypoint[1]])
    elif action == "W": return partTwo(nIndex, coordinates, [waypoint[0] - value, waypoint[1]])
    elif action == "F": 
        vectorForward = [x * value for x in waypoint]
        return partTwo(nIndex, [coordinates[0] + vectorForward[0], coordinates[1] + vectorForward[1]], waypoint)
    else:
        rotations = int(value/90)  # number of rotations of 90º in that direction
        if rotations == 2: return partTwo(nIndex, coordinates, [x * (-1) for x in waypoint]) # it rotates 180º

        if action == "L": nWaypoint = [- waypoint[1], waypoint[0]]
        elif action == "R": nWaypoint = [waypoint[1], - waypoint[0]]

        if rotations == 3: nWaypoint = [x * (-1) for x in nWaypoint]   # rotation of 270º is the negative of 90º
        return partTwo(nIndex, coordinates, nWaypoint)


with open(file) as doc:
    lines = doc.readlines()
lines = [x.strip() for x in lines]

# Part one
print("Distance for first part of the problem is " + str(partOne(0, [0, 0], [1, 0])))

# Part two
print("Distance for the second part of the problem is " + str(partTwo(0, [0, 0], [10, 1])))