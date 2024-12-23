def read(filename):
    with open(filename, 'r') as file:
        return file.readlines()
def is_inside(x,y,lines):
    return (0 <= x < len(lines[0]) and (0 <= y < len(lines)))

acc = 0
def dfs(x, y, m1, m2, index, lines):
    global acc
    letters = ['M', 'A', 'S']

    if not is_inside(x,y,lines):
        return
    if (lines[y][x] == letters[index]):
        if (index == 2):
            acc +=1
            return
        else:
            dfs(x+m1,y+m2,m1,m2,index+1,lines)

def one_star(lines):
    for line in lines:
        line = line.strip()
    for y, line in enumerate(lines):
        for x, letter in enumerate(line):
            if (letter == 'X'):
                for i in range(-1,2):
                    for j in range(-1, 2):
                        dfs(x+i,y+j,i,j,0,lines)
    return acc

def is_x_inside(x, y, lines):
    return (1 <= x < len(lines[0])-1 and 1 <= y < len(lines)-1)
def two_star(lines):
    global acc
    for line in lines:
        line = line.strip()
    for y, line in enumerate(lines):
        for x, letter in enumerate(line):
            if (letter == 'A' and is_x_inside(x,y,lines)):
                if (''.join(sorted(lines[y-1][x-1] + lines[y+1][x+1])) == "MS"
                    and ''.join(sorted(lines[y-1][x+1] + lines[y+1][x-1])) == "MS"):
                    acc+=1
    return acc

l = read('input.txt')
print(two_star(l))
