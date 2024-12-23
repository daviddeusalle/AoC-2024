import re
def read(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def one_star(lines):
    acc = 0

    for line in lines:
        items = re.findall(r"mul\((\d+),(\d+)\)", line)
        for item in items:
            acc += int(item[0]) * int(item[1])
    return acc

def two_star(lines):
    acc = 0
    status = True
    for line in lines:
        items = re.finditer(r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)", line)
        for item in items:
            if item.group(0) == "do()":
                status = True
            elif item.group(0) == "don't()":
                status = False
            else:
                if status:
                    acc += int(item.group(1)) * int(item.group(2))
    return acc
lines = read('input.txt')
print(two_star(lines))
