'''
Created on 10 dic. 2020

@author: javyn
'''
file = "input.txt"

def findTrees(lines):
    trees = 0
    squares = len(lines[0]) #    number of squares in a row
    for i in range(len(lines)):
        step = (3 * i) % squares    #    position in each line to check if there is a tree
        if (lines[i])[step] == "#":
            trees += 1
    print("The number of trees is " + str(trees))
    
def partTwo(lines):
    trees1, trees2, trees3 ,trees4 = 0, 0, 0, 0
    squares = len(lines[0]) #    number of squares in a row
    for i in range(len(lines)):
        s1, s2, s3, s4 = 1, 3, 5, 7 #    number of squares to the right in each slope
        for x in range(1, 5):
            exec("step{0} = (s{0} * i) % squares\nprint('step{0}: ' + str(step{0}))".format(x))
            exec("if (lines[i])[step{0}] == '#':\n    trees{0} += 1\nprint('trees{0}: ' + str(trees{0}))".format(x))
    print("The number of t1, t2, t3, t4 is : {0} {1} {2} and {3}".format(trees1, trees2, trees3, trees4))

with open(file) as doc:
    lines = doc.readlines()
lines = [x.strip() for x in lines]

findTrees(lines)
partTwo(lines)