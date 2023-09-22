# 탈출
from collections import deque


def bfs(end_y, end_x):

    while queue:  # 도치 길 다갔으면 끝이긴함
        node_y, node_x = queue.popleft()  # 도치 큐팝

        if (node_y, node_x) == (end_y, end_x):  # 도치가 도착하면,
            return visited[end_y][end_x]  # 도착

        # 도치 돌림, 물있으면 못감
        for delta_y, delta_x in ((1, 0), (0, 1), (-1, 0), (0, -1)):  # 즐
            (next_y, next_x) = (node_y + delta_y, node_x + delta_x)

            if 0 <= next_y < R and 0 <= next_x < C:
                # 물 퍼지는거
                if (map[next_y][next_x] == '.' or map[next_y][next_x] == 'S') and visited[next_y][next_x] == 0 and visited[node_y][node_x] == -1:
                    visited[next_y][next_x] = -1
                    queue.append((next_y, next_x))

                # 도치 퍼지는거
                if (map[next_y][next_x] == '.' or map[next_y][next_x] == 'D') and map[next_y][next_x] != 'D' \
                         and visited[node_y][node_x] != -1:
                    visited[next_y][next_x] = visited[node_y][node_x] + 1
                    queue.append((next_y, next_x))

    return 'KAKTUS'  # 못찾으면, 칵퉷


R, C = map(int, input().split())
map = [list(input()) for _ in range(R)]
queue = deque()

visited = [[0] * C for _ in range(R)]

# 물차는 걸
for i in range(R):
    for j in range(C):
        if map[i][j] == '*':
            queue.append((i, j))
            visited[i][j] = -1

# 도치 도는거
for i in range(R):
    for j in range(C):
        if map[i][j] == 'S':
            queue.append((i, j))
        elif map[i][j] == 'D':
            (end_y, end_x) = (i, j)

print(bfs(end_y, end_x))

# 물 먼저 BFS 돌리고,
# 고슴 도치 돌리고
