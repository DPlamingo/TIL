# DFS와 BFS

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in adj:
    i.sort()
# print(adj)

def DFS(start):
    stack = [start]
    visited = [0] * (N+1)
    while stack:
        now = stack.pop()
        if visited[now] == 0:
            visited[now] = 1
            print(now, end=' ')

            for next in adj[now][::-1]:
                if visited[next] == 0:
                    stack.append(next)
    # return visited
DFS(V)
print()

def BFS(start):
    queue = [start]
    visited = [0] * (N+1)
    while queue:
        now = queue.pop(0)
        if visited[now] == 0:
            visited[now] = 1
            print(now, end=' ')

            for next in adj[now]:
                if visited[next] == 0:
                    queue.append(next)

BFS(V)
print()

#
# def dfs_stack(start):
#     visited = []
#     stack = [start]
#
#     while stack:
#         now = stack.pop()
#         # 이미 방문한 지점이라면 continue
#         if now in visited:
#             continue
#
#         # 방문하지 않은 지점이라면, 방문표시
#         visited.append(now)
#
#         # 갈 수 있는 곳들을 stack 에 추가
#         for node, connection in :
#             if node == now:
#                 stack.append(connection)
#             if connection == now:
#                 stack.append(node)
#     # 출력을 위한 반환
#     return visited


# print('dfs stack = ', end='')
# print(*dfs_stack(V))
#
# def bfs_queue(start):
#     visited = []
#     queue = [start]
#
#     while queue:
#         now = queue.pop(0)
#         # 이미 방문한 지점이라면 continue
#         if now in visited:
#             continue
#
#         # 방문하지 않은 지점이라면, 방문표시
#         visited.append(now)
#
#         # 갈 수 있는 곳들을 stack 에 추가
#         for node, connection in graph:
#             if node == now:
#                 queue.append(connection)
#             if connection == now:
#                 queue.append(node)
#     # 출력을 위한 반환
#     return visited
#
#
# # print('bfs queue = ', end='')
# print(*bfs_queue(V))