'''
Created on 9 dic. 2020

@author: javyn
'''
file = "input.txt"

def validPass1(lines):
    count = 0
    
    for i in range(len(lines)):
        n1 = lines[i].split(' ')
        r = n1[0].split("-") #    range, list with first and last number
        r = [int(x) for x in r] #    convert string to int
        letter = (n1[1])[0]
        password = n1[2]
        if(password.count(letter) in range(r[0], r[1] + 1)):
            count += 1
            
    print("The number of valid password for the first excercise is {0}" .format(count))
    
def validPass2(lines):
    count = 0
    
    for i in range(len(lines)):
        n1 = lines[i].split(' ')
        r = n1[0].split("-") #    range, list with first and last number
        r = [int(x) for x in r] #    convert string to int
        letter = (n1[1])[0]
        password = n1[2]
        if (password[r[0] - 1] == letter) is not (password[r[1] - 1] == letter):
            count += 1
            
    print("The number of valid password for second excercise is {0}" .format(count))

with open(file) as doc:
    lines = doc.readlines()
        # remove `\n` at the end of each line
lines = [x.strip() for x in lines]

validPass1(lines)
validPass2(lines)
