import copy

def read(filename):
    with open(filename, 'r') as file:
        return file.read()


def find_starting_point(matrix):
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == '^':
                return (i, j)
    return None


def is_inside(x, y, matrix):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

def one_star(text):
    matrix = text.split('\n')
    visited = [[[] for _ in range(len(matrix[0]))] for _ in range(len(matrix)-1)]
    x, y = find_starting_point(matrix)
    m1 = -1
    m2 = 0
    while is_inside(x+m1, y+m2, matrix):
        visited[x][y] = True

        if matrix[x+m1][y+m2] == "#":
            m1, m2 = m2, -m1
        x+=m1
        y+=m2
    return sum(map(sum, visited)) + 1

def two_(text):
    matrix = text.split('\n')
    visited = [[[] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    x, y = find_starting_point(matrix)
    m1 = -1
    m2 = 0
    acc = 0

    while is_inside(x+m1, y+m2, matrix):
        i = x
        j = y
        aux1 = 0
        aux2 = 0
        if m1 == 1:
            aux2 = -1
        if m1 == -1:
            aux2 = 1
        if m2 == 1:
            aux1 = 1
        if m2 == -1:
            aux1 = -1
        stop = False
        while is_inside(i,j,matrix) and not stop:
            for direction in visited[i][j]:
                if direction[0] == aux1 and direction[1] == aux2:
                    acc+=1
                    stop = True
                    break
            i+=aux1
            j+=aux2
        x+=m1
        y+=m2
        visited[x][y].append([m1,m2])
        if matrix[x+m1][y+m2] == "#":
            m1, m2 = m2, -m1


    return acc

def two_star(text):
    original = text.strip().split('\n')
    acc = 0
    x1, y1= find_starting_point(original)
    for i in range(len(original)):
        for j in range(len(original[0])):
            matrix = copy.deepcopy(original)
            if original[i][j] == '^':
                continue
            row = matrix[i]
            matrix[i] = row[:j] + "#" + row[j+1:]

            visited = [[[] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

            x, y = find_starting_point(matrix)
            m1 = -1
            m2 = 0
            stop = False
            while is_inside(x+m1, y+m2, matrix) and not stop:

                while matrix[x+m1][y+m2] == "#":
                    m1, m2 = m2, -m1


                for direction in visited[x][y]:
                    if direction[0] == m1 and direction[1] == m2:
                        acc+=1
                        stop = True
                        break

                visited[x][y].append([m1,m2])
                x+=m1
                y+=m2


    return acc
text = read('input.txt')
print(two_star(text))
