from itertools import product



def read(filename):
    with open(filename, 'r') as file:
        return file.read()

def check(result, combination, numbers):
    sum = numbers[0]
    for i in range(1, len(numbers)):
        if combination[i-1] == 0:
            sum += numbers[i]
        elif combination[i-1] == 1:
            sum *= numbers[i]
        else:
            sum = int(str(sum) + str(numbers[i]))
    return result == sum



def one_star(text):
    lines = text.strip().split('\n')
    acc = 0
    for line in lines:
        parts = line.split(':')
        result = int(parts[0])
        numbers = [int(num) for num in parts[1].split()]
        n = len(numbers) - 1
        combinations = list(product([0, 1, 2], repeat=n))
        for c in combinations:
            if check(result, c, numbers):
               acc += result
               break
    return acc
text = read('input.txt')
print(one_star(text))
