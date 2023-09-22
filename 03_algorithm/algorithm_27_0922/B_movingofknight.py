# 나이트의 움직임
from collections import deque


def bfs(start_y, start_x, end_y, end_x):
    queue = deque()
    visited = [[0]*l for _ in range(l)]

    queue.append((start_y,start_x))
    visited[start_y][start_x] = 0

    while queue:
        node_y, node_x = queue.popleft()
        # print(visited)
        if (node_y, node_x) == (end_y, end_x):
            return visited[end_y][end_x]

        for delta_y, delta_x in ((2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)):
            next_y, next_x = node_y + delta_y, node_x + delta_x
            if 0 <= next_y < l and 0 <= next_x < l and visited[next_y][next_x] == 0:
                visited[next_y][next_x] = visited[node_y][node_x] + 1
                queue.append((next_y, next_x))

T = int(input())
for _ in range(T):
    l = int(input())
    start_y, start_x = map(int,input().split())
    end_y, end_x = map(int, input().split())


    print(bfs(start_y, start_x, end_y, end_x))