'''
Created on 11 dic. 2020

@author: muzta
'''
import pathlib

file = str(pathlib.Path(__file__).parent) + "\input.txt"

def groupAnswers(group):
    ans = group.split("\n") #    spliting the group into persons
    people = len(ans)   #    number of people in that griup
    ans = ''.join(ans)  #    joining all answers in a simple string
    ans = [c for c in ans]  #    list of all answers
    ansAnyone = set(ans)  #    removing repeated answers
    ansEveryone = []
    for a in ansAnyone:
        if ans.count(a) == people : ansEveryone.append(a)   #    check if the name of that answer is equal to the people of that group
    return [len(ansAnyone), len(ansEveryone)]

# List of groups
with open(file) as doc:
    d = doc.read()
groups = d.split("\n\n")
groups = [x.strip() for x in groups]


# Part one
countAnyone = 0
countEveryone = 0
for g in groups:
    countAnyone += groupAnswers(g)[0]
    countEveryone += groupAnswers(g)[1]
print("The sum of 'yes' answers by anyone is " + str(countAnyone))
print("The sum of 'yes' answers by everyone is " + str(countEveryone))