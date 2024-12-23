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


def two_star(text):
    


text = read('input.txt')
print(one_star(text))
