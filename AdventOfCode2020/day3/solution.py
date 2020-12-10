'''
Created on 10 dic. 2020

@author: javyn
'''
file = "input.txt"

def movesSlope(lines, right, down):
    trees = 0
    squares = len(lines[0])
    for i in range(0, len(lines), down):
        step = int((right * i/down) % squares)
        if (lines[i])[step] == "#":
            trees += 1
    return trees

with open(file) as doc:
    lines = doc.readlines()
lines = [x.strip() for x in lines]

# Part one
print("The number of trees is: " + str(movesSlope(lines, 3, 1)))

# Part two
mul = movesSlope(lines, 1, 1) * movesSlope(lines, 3, 1) * movesSlope(lines, 5, 1) * movesSlope(lines, 7, 1) * movesSlope(lines, 1, 2)
print("The multiplication of the number of trees is: " + str(mul))