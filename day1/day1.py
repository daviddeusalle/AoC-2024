def read(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def one_star(lines):
    sum = 0
    numbers1 = []
    numbers2 = []
    for line in lines:
        parts = line.split("   ")
        numbers1.append(int(parts[0]))
        numbers2.append(int(parts[1]))
    print(numbers1)
    numbers1 = sorted(numbers1)
    numbers2 = sorted(numbers2)
    for i in range(len(numbers1)):
        sum += abs(numbers1[i] - numbers2[i])
    return sum

def two_star(lines):
    left = []
    right = {}
    sum = 0
    for line in lines:
        parts = line.split("   ")
        num1 = int(parts[0])
        num2 = int(parts[1])
        left.append(num1)
        if num2 in right:
            right[num2] += 1
        else:
            right[num2] = 1
    for num in left:
        if num in right:
            sum += (right[num] * num)
    return sum

lines = read('input.txt')
print(two_star(lines))
