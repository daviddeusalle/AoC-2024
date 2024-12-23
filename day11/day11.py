import math


def read(filename):
    with open(filename, 'r') as file:
        return file.read()


def one_star(line):
    numbers = [int(char) for char in line.strip().split()]
    for i in range(0,25):
        tmp = []
        for j in range(len(numbers)):
            size = len(str(numbers[j]))

            if numbers[j] == 0:
                tmp.append(1)
            elif size % 2 == 0:
                tmp.append(int(str(numbers[j])[:int(size/2)]))
                tmp.append(int(str(numbers[j])[int(size/2):]))
            else:
                tmp.append(numbers[j]*2024)

        numbers = tmp
    return len(numbers)


max_level = 75
memo = {}


def blink(number, level):
    if number == -1:
        return 0
    if (number, level) in memo:
        return memo[(number, level)]

    if level == max_level:
        return 1
    size = len(str(number))
    left = -1
    right = -1
    if number == 0:
        left = 1
    elif size % 2 == 0:
        left = int(str(number)[:size // 2])
        right = int(str(number)[size // 2:])
    else:
        left = number * 2024
    memo[(number, level)] = blink(left, level+1) + blink(right, level+1)
    return memo[(number, level)]


def two_star(line):
    numbers = [int(char) for char in line.strip().split()]
    acc = 0
    for number in numbers:
        acc += blink(number, 0)
    return acc

text = read('input.txt')
print(two_star(text))
