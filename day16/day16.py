import heapq

def read(filename):
    with open(filename, 'r') as file:
        return file.read()


def find_starting_point(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "S":
                return i,j
    assert("No starting point found")
    return None


def dijkstra(matrix, start):
    rows, cols = len(matrix), len(matrix[0])
    x, y, dx, dy = start
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Este, Sur, Oeste, Norte

    # Distancia mínima para (x, y, dirección)
    distances = {}
    for i in range(rows):
        for j in range(cols):
            for d in directions:
                distances[(i, j, d)] = float('inf')

    distances[(x, y, (dx, dy))] = 0
    pq = [(0, x, y, dx, dy)]  # (costo, x, y, dx, dy)

    while pq:
        cost, x, y, dx, dy = heapq.heappop(pq)

        # Si llegamos al final
        if matrix[x][y] == "E":
            return cost

        # Si ya tenemos un mejor costo, continuamos
        if cost > distances[(x, y, (dx, dy))]:
            continue

        # Intenta moverse hacia adelante
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] != "#":
            new_cost = cost + 1
            if new_cost < distances[(nx, ny, (dx, dy))]:
                distances[(nx, ny, (dx, dy))] = new_cost
                heapq.heappush(pq, (new_cost, nx, ny, dx, dy))

        # Gira a la derecha o izquierda
        for ndx, ndy in [(dy, -dx), (-dy, dx)]:  # Gira derecha y izquierda
            if distances[(x, y, (ndx, ndy))] > cost + 1000:
                distances[(x, y, (ndx, ndy))] = cost + 1000
                heapq.heappush(pq, (cost + 1000, x, y, ndx, ndy))

    return float('inf')

def dijkstra(matrix, start):
    rows, cols = len(matrix), len(matrix[0])
    x, y, dx, dy = start
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    distances = {}
    for i in range(rows):
        for j in range(cols):
            for d in directions:
                distances[(i, j, d)] = float('inf')

    distances[(x, y, (dx, dy))] = 0
    pq = [(0, x, y, dx, dy)]

    while pq:
        cost, x, y, dx, dy = heapq.heappop(pq)

        if matrix[x][y] == "E":
            return cost

        if cost > distances[(x, y, (dx, dy))]:
            continue

        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] != "#":
            new_cost = cost + 1
            if new_cost < distances[(nx, ny, (dx, dy))]:
                distances[(nx, ny, (dx, dy))] = new_cost
                heapq.heappush(pq, (new_cost, nx, ny, dx, dy))

        for ndx, ndy in [(dy, -dx), (-dy, dx)]:
            if distances[(x, y, (ndx, ndy))] > cost + 1000:
                distances[(x, y, (ndx, ndy))] = cost + 1000
                heapq.heappush(pq, (cost + 1000, x, y, ndx, ndy))

    return float('inf')

def one_star(input):
    parts = input.split("\n")
    matrix = [list(row) for row in parts]
    x,y = find_starting_point(matrix)
    return dijkstra(matrix, (x,y,0,1))


text = read('day16/input.txt')
print(one_star(text))
