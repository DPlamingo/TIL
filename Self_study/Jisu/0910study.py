# 백준 실3 컴퓨터 바이러스 DFS

N = int(input()) # 컴퓨터 수
CN = int(input()) # 컴퓨터 쌍의 수
com = [list(map(int, input().split())) for _ in range(CN)]

stack = [1]
visited = [1]

while stack:
    node = stack.pop()
    for y,x in com:
        if y == node and x not in visited:
            stack.append(x)
            visited.append(x)
        elif x == node and y not in visited:
            stack.append(y)
            visited.append(y)

# print(visited)
result = len(visited) - 1
print(result)