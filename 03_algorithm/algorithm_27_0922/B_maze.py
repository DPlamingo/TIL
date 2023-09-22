# 미로탐색
from collections import deque


def bfs(start_y, start_x, end_y, end_x):
    queue = deque()

    visited = [[0] * M for _ in range(N)]

    queue.append((start_y,start_x))
    # print(queue)
    visited[start_y][start_x] = 1
    # print(graph)
    # print(visited)

    while queue:
        nodey, nodex = queue.popleft()
        if (nodey, nodex) == (end_y, end_x): # 정답
            return visited[end_y][end_x]

        for dy, dx in delta:
            next_y, next_x = dy+nodey, dx+nodex
            if 0 <= next_y < N and 0 <= next_x < M and graph[next_y][next_x] == 1 and visited[next_y][next_x] == 0:
                queue.append((next_y,next_x))
                visited[next_y][next_x] = visited[nodey][nodex] + 1



delta = [[1,0],[-1,0],[0,1],[0,-1]]

N, M = map(int, input().split())
graph = [list(map(int,input())) for _ in range(N)]

result = bfs(0, 0, N-1, M-1)
print(result)