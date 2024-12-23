import re

with open('input.txt', 'r') as file:
    lines = file.readlines()

patterns = lines[0].strip().split(', ')
designs = [line.strip() for line in lines[2:]]

def arrange(design, patterns):
    flag = False
    if design == "":
        return True
    for pattern in patterns:
        if design[:len(pattern)] == pattern:
            flag = arrange(design[len(pattern):], patterns)
            if flag:
                return True

    return False

def one_star():
    acc = 0
    for design in designs:
        if arrange(design, patterns):
            acc += 1
    return acc

memo = {}
def arrange2(design, patterns):
    counter = 0
    if design == "":
        return 1
    if design in memo:
        return memo[design]
    for pattern in patterns:
        if design[:len(pattern)] == pattern:
            counter += arrange2(design[len(pattern):], patterns)
    memo[design] = counter
    return counter

def two_star():
    acc = 0
    for design in designs:
        acc+=arrange2(design, patterns)
    return acc

print(two_star())
