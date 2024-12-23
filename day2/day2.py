def read(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def is_save(num1, num2):
    return 1 <= abs(num1-num2) <= 3

def one_star(lines):
    sum = 0

    for line in lines:
        parts = line.split(" ")
        save = True
        numbers = [int(part) for part in parts]

        for i in range(len(numbers)-1):
            if i > 0 and not (numbers[i-1] <= numbers[i] <= numbers[i+1] or numbers[i-1] >= numbers[i] >= numbers[i+1]):
                save = False
            if not is_save(numbers[i], numbers[i+1]):
                save = False
        if save:
            sum+= 1
    return sum

def is_correct(numbers):
    save = True
    for i in range(len(numbers)-1):
            if i > 0 and not (numbers[i-1] <= numbers[i] <= numbers[i+1] or numbers[i-1] >= numbers[i] >= numbers[i+1]):
                save = False
            if not is_save(numbers[i], numbers[i+1]):
                save = False
    return save



def two_star(lines):
    sum = 0

    for line in lines:
        parts = line.split(" ")

        numbers = [int(part) for part in parts]
        i = 0
        for i in range(len(numbers)):
            copy = numbers.copy()
            del copy[i]
            if is_correct(copy):
                sum+= 1
                break


    return sum

lines = read('input.txt')
print(one_star(lines))
print(two_star(lines))
