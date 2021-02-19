'''
Created on 8 dic. 2020

@author: muzta
'''
import pathlib

targetNumber = 2020
file = str(pathlib.Path(__file__).parent) + "\input.txt"

def find2Numbers(numbers):
    for i in range(len(numbers)):
        n1 = int(numbers[i])
        for x in range(i + 1, len(numbers)):
            n2 = int(numbers[x])
            if(n1 + n2) == targetNumber:
                multiply2(n1, n2)
                break

def multiply2(number1, number2):
    mul = number1 * number2
    print("    Solution 1    \nThe numbers to multiply are: {0} and {1} \nAnd the result is {2}" .format(str(number1), str(number2), str(mul)))

def find3Numbers(numbers):
    for x in range(len(numbers)):
        n1 = int(numbers[x])
        for y in range(x + 1, len(numbers)):
            n2 = int(numbers[y])
            if(n1 + n2) < targetNumber: #    only continue if the sum is not the target number yet
                for z in range(y + 1, len(numbers)):
                    n3 = int(numbers[z])
                    if(n1 + n2 + n3) == targetNumber:
                        multiply3(n1, n2, n3)
                        break


def multiply3(number1, number2, number3):
    mul = number1 * number2 * number3
    print("    Solution 2    \nThe numbers to multiply are: {0}, {1} and {2} \nAnd the result is {3}" .format(str(number1), str(number2), str(number3), str(mul)))

with open(file) as doc:
    numbers = doc.readlines()
numbers = [x.strip() for x in numbers]  # remove `\n` at the end of each line

find2Numbers(numbers)
find3Numbers(numbers)