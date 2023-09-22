from collections import deque

def bfs(start_y, start_x, end_y, end_x, water_y, water_x):
    queue_water = deque()
    queue_dochi = deque()
    visited = [[0] * C for _ in range(R)]

    queue_water.append((water_y, water_x))
    queue_dochi.append((start_y, start_x))
    visited[water_y][water_x] = False

    while queue_dochi:
        if queue_water:
            flood_y, flood_x = queue_water.popleft()
        node_y, node_x = queue_dochi.popleft()

        if (node_y, node_x) == (end_y, end_x):
            return visited[end_y][end_x]

        for delta_y, delta_x in ((1,0),(0,1),(-1,0),(0,-1)):
            next_water_y, next_water_x = flood_y + delta_y, flood_x + delta_x

            if 0 <= next_water_y < R and 0 <= next_water_x < C and map[next_water_y][next_water_x] == '.' and visited[next_water_y][next_water_x] == 0:
                visited[next_water_y][next_water_x] = False
                queue_water.append((next_water_y, next_water_x))

        for delta_y, delta_x in ((1,0),(0,1),(-1,0),(0,-1)):
            next_y, next_x = node_y + delta_y, node_x + delta_x

            if 0 <= next_y < R and 0 <= next_x < C and visited[next_y][next_x] == 0 and map[next_y][next_x] == '.':
                visited[next_y][next_x] = visited[node_y][node_x] + 1
                queue_dochi.append((next_y, next_x))

    return 'KAKTUS'

R, C = map(int, input().split())
map = [list(input()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        if map[i][j] == 'S':
            start_y, start_x = i, j
        elif map[i][j] == 'D':
            end_y, end_x = i, j
        elif map[i][j] == '*':
            water_y, water_x = i, j

print(bfs(start_y, start_x, end_y, end_x, water_y, water_x))
