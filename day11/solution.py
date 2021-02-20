'''
Created on 7 feb. 2021

@author: javyn
'''
import pathlib

file = str(pathlib.Path(__file__).parent) + "\input.txt"

def partOne(lines):
    newLines = [row[:] for row in lines]    # create a copy of a 2D array
    noMoreChanges = True    # if people has stopped moving

    for r in range(rowSize):
        for c in range(columnSize):

            nAdjacentSeats = 0
            actPosition = lines[r][c]   # current position
            
            if actPosition != ".":  # if the seat can be occupied
                
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x == y == 0: continue    # it cant be the same position
                        row = r + x
                        column = c + y
                        if (row >= 0 and row < rowSize) and (column >= 0 and column < columnSize) :    # it is in the limit of the input
                            if lines[row][column] == "#": nAdjacentSeats += 1
                        
                if actPosition == "L" and nAdjacentSeats == 0: 
                    newLines[r][c] = "#"
                    noMoreChanges = False
                elif actPosition == "#" and nAdjacentSeats > 3:
                    newLines[r][c] = "L"
                    noMoreChanges = False
                 
    if noMoreChanges == False: return partOne(newLines)
    else: return countSeatsOccupied(newLines)

def countSeatsOccupied(lines):
    count = 0
    for l in lines:
        count += l.count("#")
    return count

def partTwo(lines):
    newLines = [row[:] for row in lines]    # create a copy of a 2D array
    noMoreChanges = True    # if people has stopped moving

    for r in range(rowSize):
        for c in range(columnSize):

            nAdjacentSeats = 0
            actPosition = lines[r][c]
            
            if actPosition != ".":  # if the seat can be occupied
                
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x == y == 0: continue    # it cant be the same position
                        row = r
                        column = c
                        while True:
                            row += x
                            column += y
                            if (row < 0 or row >= rowSize) or (column < 0 or column >= columnSize): break   # it is not in the limit of the input
                            if lines[row][column] != ".":  # check the first seat seen
                                if lines[row][column] == "#": 
                                    nAdjacentSeats += 1
                                break

                if actPosition == "L" and nAdjacentSeats == 0: 
                    newLines[r][c] = "#"
                    noMoreChanges = False
                elif actPosition == "#" and nAdjacentSeats > 4:
                    newLines[r][c] = "L"
                    noMoreChanges = False
         
    if noMoreChanges == False: return partTwo(newLines)
    else: return countSeatsOccupied(newLines)


with open(file) as doc:
    lines = doc.readlines()
lines = [x.strip() for x in lines]
lines = [list(x) for x in lines]

rowSize = len(lines) # number of rows
columnSize = len(lines[0]) # number of columns

#Part one
print("The number of seats occupied in part one is : " + str(partOne(lines)))

#Part two
print("The number of seats occupied in the second part is : " + str(partTwo(lines)))