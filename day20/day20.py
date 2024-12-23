from collections import deque

matrix = [line.strip() for line in open('input.txt')]

H = len(matrix)
W = len(matrix[0])

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def find_points():

    s, e = None, None
    for i in range(H):
        for j in range(W):
            if matrix[i][j] == "S":
                s = (i,j)
            if matrix[i][j] == "E":
                e = (i,j)
            if s and e:
                break
    return s, e

def is_inside(x, y):
    return 0 <= x < H and 0 <= y < W

def solve(picoseconds):
    s, e = find_points()
    x, y = s
    distance = 0

    distances = {(i, j): float('inf') for i in range(H+1) for j in range(W+1)}
    distances[s] = 0


    while (x,y) != e:
        distance += 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if is_inside(nx, ny) and matrix[nx][ny] != "#" and distances[(nx, ny)] > distance:
                distances[(nx, ny)] = distance
                x, y = nx, ny
                break

    x, y = s
    acc = 0
    distance = 0
    while (x,y) != e:

        acc += cheat(x, y, distance, distances, picoseconds)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if matrix[nx][ny] != "#" and distances[(nx, ny)] > distances[(x, y)]:
                x, y = nx, ny

                break
        distance += 1

    return acc


def cheat(x0, y0, distance, distances, picoseconds):
    visited = set()
    cheats = 0
    queue = deque([(x0, y0)])
    while queue:
        x, y,  = queue.popleft()


        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_inside(nx, ny) and not (nx, ny) in visited:
                dist = abs(nx - x0) + abs(ny - y0)

                if dist <= picoseconds:
                    visited.add((nx,ny))
                    queue.append((nx, ny))
                    if distance + dist <= distances[(nx, ny)] -100 and matrix[nx][ny] != "#":
                        cheats+=1
    return cheats


print("Part 1: ", solve(2))
print("Part 2: ", solve(20))
