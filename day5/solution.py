'''
Created on 11 dic. 2020

@author: muzta
'''
import pathlib

file = str(pathlib.Path(__file__).parent) + "\input.txt"
nRows = 128
nColumns = 8

def seatPosition(seat, i, minR, maxR, minC, maxC):
    #    recursion
    if i < (len(seat)):
        c = seat[i] #    char at that position
        i += 1
        if c == "F" :
            return seatPosition(seat, i, minR, minR + int((maxR-minR)/2), minC, maxC)
        elif c == "B":
            return seatPosition(seat, i, minR + 1 + int((maxR-minR)/2), maxR, minC, maxC)
        elif c == "L":
            return seatPosition(seat, i, minR, maxR, minC, minC + int((maxC-minC)/2))
        elif c == "R":
            return seatPosition(seat, i, minR, maxR, minC  + 1 + int((maxC-minC)/2), maxC)
    else:
        return [maxR, maxC]
            
with open(file) as doc:
    seats = doc.readlines()
seats = [x.strip() for x in seats]

# Part one
listID = []
for s in seats:
    sp = seatPosition(s, 0, 0, nRows - 1, 0, nColumns - 1)
    seatId = sp[0] * 8 + sp[1]
    listID.append(seatId)
print("The highest seat id is: " + str(max(listID)))

# Part two
listID.sort()
for i in listID:
    if listID[i + 1] != listID[i] + 1:  #    check the next seat id is same as the sum of the current one plus one; if not, that will be empty
        print("Your seat is " + str(listID[i] + 1))
        break