'''
Created on 11 dic. 2020

@author: muzta
'''
file = "input.txt"
goalBag = "shiny gold"

def bagContains(rule):
    bags = rule.split("contain")
    original = bags[0].replace("bags", "").strip()  # color of the original bag i'm checking
    
    if "no other bags" in bags[1] : return [original, []]
    
    listBags = bags[1].strip().replace(".", "").replace("bags", "").replace("bag", "") # delete the point and word bag(s) from the string
    
    contains = listBags.split(",")
    contains = [x.strip() for x in contains]
    colorBags = []  # list of color of the bags the original can hold
    for b in contains:
        colorBags.append(b)
        
    return [original, colorBags]    # return the original color and the list of color it can hold

def canContain(goalBag, dictionary, current):   # check if the given bag ('current') can contain the goal bag
    colorList = [x[2:] for x in dictionary[current]]
    if goalBag in colorList : return 1    # if goalbag if in the list of the current bag, return 1
    else : 
        for b in colorList:
            canThis = canContain(goalBag, dictionary, b)    # iterate over the colors the current bag can hold
            if canThis : return 1
            
        return 0    # if goalbag doesn't appear, return 0
    
def numberBags(bag, dictionary):
    numberList = [x[0] for x in dictionary[bag]]
    colorList = [x[2:] for x in dictionary[bag]]
    
    count = 1   # the bag itself
    
    for i in range(len(colorList)):
        number = int(numberList[i])
        color = colorList[i]
        
        count += number * numberBags(color, dictionary)
    
    return count
    
with open(file) as doc:
    rules = doc.readlines()
rules = [x.strip() for x in rules]
    
# Create dictionary with all bags and the one they can hold
d = {}
for r in rules:
    d[bagContains(r)[0]] = bagContains(r)[1]
    
# print(d)
count = 0
for i in d:
    count += canContain(goalBag, d, i)
print("A total of {0} bags can contain a shiny gold bag".format(count))

# Part two
nbag = numberBags(goalBag, d) - 1   # to discount the shiny gold bag
print("The number of individual bags required is " + str(nbag))