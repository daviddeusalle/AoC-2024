import re

def read(filename):
    with open(filename, 'r') as file:
        return file.read()

size_x = 101
size_y = 103
seconds = 10
def one_star(input):
    lines = input.strip().split("\n")
    quadrants = [0,0,0,0]
    acc = 1
    for line in lines:

        numbers = re.findall(r'[-+]?\d+', line)
        x = int(numbers[0])
        y = int(numbers[1])
        vx = int(numbers[2])
        vy = int(numbers[3])
        new_x = (vx*seconds +x) % size_x
        new_y = (vy*seconds +y) % size_y
        if new_x < (size_x // 2) and new_y < (size_y // 2):
            quadrants[0]+=1
        if new_x < (size_x // 2) and new_y > (size_y // 2):
            quadrants[1]+=1
        if new_x > (size_x // 2) and new_y < (size_y // 2):
            quadrants[2]+=1
        if new_x > (size_x // 2) and new_y > (size_y // 2):
            quadrants[3]+=1

    for quadrant in quadrants:
        acc*=quadrant
    return acc

def two_star(input):
    lines = input.strip().split("\n")
    x = []
    y = []
    vx = []
    vy = []

    for line in lines:

        numbers = re.findall(r'[-+]?\d+', line)
        x.append(int(numbers[0]))
        y.append(int(numbers[1]))
        vx.append(int(numbers[2]))
        vy.append(int(numbers[3]))
    best = 10000000000
    index = 0
    for i in range(10000):
        quadrants = [0,0,0,0]
        acc = 1
        for j in range(len(x)):

            new_x = (vx[j]*i +x[j]) % size_x
            new_y = (vy[j]*i +y[j]) % size_y
            if new_x < (size_x // 2) and new_y < (size_y // 2):
                quadrants[0]+=1
            if new_x < (size_x // 2) and new_y > (size_y // 2):
                quadrants[1]+=1
            if new_x > (size_x // 2) and new_y < (size_y // 2):
                quadrants[2]+=1
            if new_x > (size_x // 2) and new_y > (size_y // 2):
                quadrants[3]+=1
        for quadrant in quadrants:
            acc*=quadrant
        if acc < best:
            best = acc
            index = i
    return index


text = read('input.txt')
print(two_star(text))
