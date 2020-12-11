import re
'''
Created on 10 dic. 2020

@author: javyn
'''
file = "input.txt"

def hasAllFields(passport):
    valid = "byr:" in passport and "iyr:" in passport and "eyr" in passport and "hgt" in passport
    valid = valid and "hcl" in passport and "ecl" in passport and "pid" in passport
    return valid
    
def isValid(passport):
    # Regular expressions
    rBirth = "^(\d{4})$"
    rIssueYear = "^(\d{4})$"
    rExpYear = "^(\d{4})$"
    rHeight = "^(\d{3}(cm)|\d{2}(in))$" #    check ranges depending if it is cm or in
    rHairColor = "^\#[0-9a-f]{6}$"
    rEyeColor = "^(amb|blu|brn|gry|grn|hzl|oth)$"
    rPassport = "^\d{9}$"
    
    variables = re.split(" |\n", passport)
    d = {}  #    instantiate dictionary
    for v in variables:
        keyValue = v.split(":")
        d[keyValue[0]] = keyValue[1]
    
    valid = re.search(rBirth, d["byr"]) and 1920 <= int(d["byr"]) <= 2002
    valid = valid and re.search(rIssueYear, d["iyr"]) and 2010 <= int(d["iyr"]) <= 2020
    valid = valid and re.search(rExpYear, d["eyr"]) and 2020 <= int(d["eyr"]) <= 2030
    valid = valid and re.search(rHeight, d["hgt"])
    if valid:
        if "cm" in d["hgt"] : 
            valid = valid and (150 <= int(d['hgt'][:-2]) <= 193)
        else:
            valid = valid and (59 <= int(d['hgt'][:-2]) <= 76)
    valid = valid and re.search(rHairColor, d["hcl"])
    valid = valid and re.search(rEyeColor, d["ecl"])
    valid = valid and re.search(rPassport, d["pid"])
    
    return bool(valid)

# List of passports, splitting the document by break line
with open(file) as doc:
    d = doc.read()
passports = d.split("\n\n")
passports = [x.strip() for x in passports]

# Part one
count = 0
for p in passports:
    if hasAllFields(p) : count += 1
print("The number of passwords with all fields is " + str(count))

# Part two
count = 0
for p in passports:
    if hasAllFields(p):
        if isValid(p) : count += 1
print("The number of valid passwords is " + str(count))