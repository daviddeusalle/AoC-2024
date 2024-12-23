import re
from sympy import symbols, Eq, solve


def read(filename):
    with open(filename, 'r') as file:
        return file.read()


def find_robot(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "@":
                return i, j
    return None


def push(x, y, dx, dy, matrix):
    x+=dx
    y+=dy
    if matrix[x][y] == "#":
        return False
    elif matrix[x][y] == "O":
        move = push(x,y,dx,dy,matrix)
        if move:
            matrix[x][y] = matrix[x - dx][y - dy]
        return move
    elif matrix[x][y] == ".":
        matrix[x][y] = matrix[x-dx][y-dy]
        return True

def one_star(text):
    parts = text.strip().split("\n\n")
    acc = 0
    matrix = [list(sub) for sub in parts[0].split("\n")]
    moves = parts[1]

    x, y = find_robot(matrix)

    for move in moves:
        dx, dy = 0,0
        if move == "<":
            dx = 0
            dy = -1
        elif move == "^":
            dx = -1
            dy = 0
        elif move == ">":
            dx = 0
            dy = 1
        elif move == "v":
            dx= 1
            dy = 0
        moved = push(x, y, dx, dy, matrix)
        if moved:
            matrix[x][y] = "."
            x+=dx
            y+=dy


    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "O":
                acc += 100*i + j
    return acc


def can_move(x,y,dx,dy,matrix, visited):
    if (x,y) in visited:
        return True
    visited.add((x, y))
    x += dx
    y += dy



    if matrix[x][y] == "#":
        return False
    elif matrix[x][y] == "[":
        return (can_move(x, y, dx, dy, matrix,visited) and can_move(x, y+1, dx, dy, matrix,visited))
    elif matrix[x][y] == "]":
        return (can_move(x, y, dx, dy, matrix,visited) and can_move(x, y-1, dx, dy, matrix,visited))
    elif matrix[x][y] == ".":
        return True

def update_v(x, y, dx, dy, matrix, visited):
    if (x,y) in visited:
        return
    visited.add((x,y))
    x += dx
    y += dy
    if matrix[x][y] == "#":
        return False
    elif matrix[x][y] == "[":
        update_v(x, y, dx, dy, matrix,visited)
        update_v(x, y+1, dx, dy, matrix,visited)

        if (x - dx, y - dy) in visited:
            matrix[x][y] = matrix[x - dx][y - dy]
        else:
            matrix[x][y] = "."
        if (x - dx, y - dy +1) in visited:
            matrix[x][y +1] = matrix[x - dx][y - dy + 1]
        else:
            matrix[x][y+1] = "."

        
    elif matrix[x][y] == "]":

        update_v(x, y, dx, dy, matrix,visited)
        update_v(x, y-1, dx, dy, matrix,visited)
        if (x - dx, y - dy) in visited:
            matrix[x][y] = matrix[x - dx][y - dy]
        else:
            matrix[x][y] = "."
        if (x - dx, y - dy - 1) in visited:
            matrix[x][y - 1] = matrix[x - dx][y - dy - 1]
        else:
            matrix[x][y - 1] = "."


    elif matrix[x][y] == ".":
        matrix[x][y] = matrix[x-dx][y-dy]

def update_h(x, y, dx, dy, matrix):
    x += dx
    y += dy
    if matrix[x][y] == "#":
        return False
    elif matrix[x][y] == "[" or matrix[x][y] == "]":
        update_h(x, y, dx, dy, matrix)
        matrix[x][y] = matrix[x-dx][y-dy]

    elif matrix[x][y] == ".":
        matrix[x][y] = matrix[x-dx][y-dy]

def two_star(input):
    matrix = []
    parts = input.strip().split("\n\n")
    for r in parts[0].split("\n"):
        row = []
        for e in r:
            if e == "#":
                row.extend("##")
            elif e == "O":
                row.extend("[]")
            elif e == ".":
                row.extend("..")
            elif e == "@":
                row.extend("@.")
        matrix.append(list(row))
    x, y = find_robot(matrix)
    moves = parts[1]

    for move in moves:
        dx, dy = 0, 0
        if move == "<":
            dx = 0
            dy = -1
        elif move == "^":
            dx = -1
            dy = 0
        elif move == ">":
            dx = 0
            dy = 1
        elif move == "v":
            dx = 1
            dy = 0

        moved = can_move(x, y, dx, dy, matrix, set())
        if moved:

            if dx != 0:
                update_v(x, y, dx, dy, matrix,set())
            else:
                update_h(x,y,dx,dy,matrix)
            matrix[x][y] = "."
            x += dx
            y += dy
    acc = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "[":
                acc += 100*i + j
    return acc


text = read('input.txt')
print(two_star(text))