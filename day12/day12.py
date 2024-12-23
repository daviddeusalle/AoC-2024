def read(filename):
    with open(filename, 'r') as file:
        return file.read()


def is_inside(x, y, matrix):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

def one_star(text):
    matrix = text.strip().split("\n")
    visited = set()
    count = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            area = 0
            perimeter = 0
            def dfs(i, j, letter):
                nonlocal perimeter, area

                if not is_inside(i,j,matrix) or matrix[i][j] != letter:
                    perimeter+=1
                    return
                if (i, j) in visited:
                    return
                visited.add((i,j))
                dfs(i-1, j, letter)
                dfs(i+1, j, letter)
                dfs(i, j-1, letter)
                dfs(i, j+1, letter)
                area+=1
            if (x,y) not in visited:
                dfs(x,y, matrix[x][y])
                count += area*perimeter
    return count


def get_borders(matrix):
    borders = []
    for x in range(len(matrix)):
        row = []
        for y in range(len(matrix[0])):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            letter = matrix[x][y]
            element_borders = []
            for dx, dy in directions:
                element_borders.append( not is_inside(x+dx,y+dy,matrix) or matrix[x+dx][y+dy] != letter)
            row.append(element_borders)
        borders.append(row)
    return borders


def update_borders(x, y, dx, dy, border, letter, matrix, borders):
    while is_inside(x,y,matrix) and matrix[x][y] == letter and borders[x][y][border]:
        borders[x][y][border] = False
        x+=dx
        y+=dy

def two_star(text):
    matrix = text.strip().split("\n")
    borders = get_borders(matrix)
    count = 0
    visited = set()

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            sides = 0
            area = 0

            def dfs(i, j, letter):
                nonlocal sides, area

                if not is_inside(i,j,matrix) or matrix[i][j] != letter:
                    return
                if (i, j) in visited:
                    return
                for index, border in enumerate(borders[i][j]):
                    if border:
                        sides+=1
                        borders[i][j][index] = False
                        if index == 0 or index == 1:
                            update_borders(i,j-1, 0, -1, index, letter, matrix, borders)
                            update_borders(i,j+1, 0, 1, index, letter, matrix, borders)
                        else:
                            update_borders(i-1, j, -1, 0, index, letter, matrix, borders)
                            update_borders(i+1, j, 1, 0, index, letter, matrix, borders)

                visited.add((i,j))
                dfs(i-1, j, letter)
                dfs(i+1, j, letter)
                dfs(i, j-1, letter)
                dfs(i, j+1, letter)
                area+=1
            if (x, y) not in visited:

                dfs(x, y, matrix[x][y])
                count += area * sides

    return count






text = read('input.txt')
print(two_star(text))