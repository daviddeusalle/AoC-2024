


def read(filename):
    with open(filename, 'r') as file:
        return file.read()


def is_inside(x, y, matrix):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

def one_star(text):
    antenas = {}
    antinodes = {}
    lines = text.strip().split('\n')
    for i, line in enumerate(lines):
        for j, element in enumerate(line):
            if element != '.':
                if element not in antenas:
                    antenas[element] =  []

                antenas[element].append((i,j))
    for key, items in antenas.items():
        for i in range(len(items)):
            for j in range(len(items)):
                if i == j:
                    continue
                dx = (items[i][0] - items[j][0])*2 + items[j][0]
                dy = (items[i][1] - items[j][1])*2 + items[j][1]
                if is_inside(dx, dy, lines):
                    if (dx, dy) not in antinodes:
                        antinodes[(dx,dy)] = True
    print(antinodes)
    return len(antinodes)

def two_star(text):
    antenas = {}
    antinodes = {}
    lines = text.strip().split('\n')
    for i, line in enumerate(lines):
        for j, element in enumerate(line):
            if element != '.':
                if element not in antenas:
                    antenas[element] =  []

                antenas[element].append((i,j))
    for key, items in antenas.items():
        for i in range(len(items)):
            for j in range(len(items)):
                if i == j:
                    continue
                dx = (items[i][0] - items[j][0])
                dy = (items[i][1] - items[j][1])
                x = dx + items[j][0]
                y = dy + items[j][1]
                while is_inside(x, y, lines):
                    if (x, y) not in antinodes:
                        antinodes[(x,y)] = True
                    x += dx
                    y += dy
    return len(antinodes)




text = read('input.txt')
print(two_star(text))
