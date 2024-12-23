import re
import heapq

H = 70
W = 70
N = 1024
coords= [list(map(int, re.findall(r'\d+', line)))
             for line in open('input.txt')]
corrupted = set()
for i in range(N):
    corrupted.add((coords[i][0], coords[i][1]))


def is_inside(x, y):
    return 0 <= x <= H and 0 <= y <= W


def dijkstra():
    x, y = 0, 0
    distances = {(i, j): float('inf') for i in range(H+1) for j in range(W+1)}
    distances[(x, y)] = 0
    pq = [(0, (x,y))]

    while pq:
        current_distance, (x, y) = heapq.heappop(pq)
        if x == H and y == W:
            return current_distance

        if current_distance > distances[(x, y)]:
            continue
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            distance = current_distance + 1
            if is_inside(nx, ny) and (nx, ny) not in corrupted and distance < distances[(nx, ny)]:
                distances[(nx, ny)] = distance
                heapq.heappush(pq, (distance, (nx, ny)))

    return float('inf')


print(dijkstra())