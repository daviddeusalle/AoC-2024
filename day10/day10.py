def read(filename):
    with open(filename, 'r') as file:
        return file.readlines()


def is_inside(x, y, matrix):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])


def one_star(text):
    matrix = [[int(char) for char in line.strip()] for line in text]
    score = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            visited = set()

            def dfs(i, j, number):
                nonlocal score
                if not is_inside(i,j,matrix) or (i,j) in visited:
                    return

                if matrix[i][j] == number:
                    if number == 9:
                        visited.add((i,j))
                        score +=1
                        return
                    number+=1
                    dfs(i-1, j, number)
                    dfs(i, j+1, number)
                    dfs(i+1, j, number)
                    dfs(i, j-1, number)

                    visited.add((i,j))

            dfs(x, y, 0)

    return score


def two_star(text):
    matrix = [[int(char) for char in line.strip()] for line in text]
    score = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):

            def dfs(i, j, number):
                nonlocal score
                if not is_inside(i,j,matrix):
                    return

                if matrix[i][j] == number:
                    if number == 9:
                        score +=1
                        return
                    number+=1
                    dfs(i-1, j, number)
                    dfs(i, j+1, number)
                    dfs(i+1, j, number)
                    dfs(i, j-1, number)


            dfs(x, y, 0)

    return score

lines = read('input.txt')
print(two_star(lines))