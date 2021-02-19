'''
Created on 7 feb. 2021

@author: javyn
'''
import pathlib

file = str(pathlib.Path(__file__).parent) + "\input.txt"

def partOne(lines):
    newLines = [row[:] for row in lines]    # create a copy of a 2D array
    noMoreChanges = True    # if people has stopped moving
    rowSize = len(lines) # number of rows
    columnSize = len(lines[0]) # number of columns

    for r in range(rowSize):
        for c in range(columnSize):

            nAdjacentSeats = 0
            actPosition = lines[r][c]
            
            if actPosition != ".":  # if the seat can be occupied
                
                for x in range(-1, 2):
                    for y in range(-1, 2):
                            row = r + x
                            column = c + y
                            if (row >= 0 and row < rowSize) and (column >= 0 and column < columnSize) and not (row == r and column == c) :    # for no checking the same position
                                if lines[row][column] == "#": nAdjacentSeats += 1
                        
                if actPosition == "L" and nAdjacentSeats == 0: 
                    newLines[r][c] = "#"
                    noMoreChanges = False
                elif actPosition == "#" and nAdjacentSeats > 3:
                    newLines[r][c] = "L"
                    noMoreChanges = False
                 
    if noMoreChanges == False: return partOne(newLines)
    else:
        count = 0
        for l in newLines:
            count += l.count("#")
        return count


with open(file) as doc:
    lines = doc.readlines()
lines = [x.strip() for x in lines]
lines = [list(x) for x in lines]


#Part one
print("The number of seats occupied is : " + str(partOne(lines)))