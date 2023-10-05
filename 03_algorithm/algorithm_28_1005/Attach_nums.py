    # attach_nums

def dfs(i,j):
    stack = [(i,j)]
    visited = []
    while stack:
        nodei, nodej = stack.pop()
        if (nodei,nodej) not in visited:
            arr[nodei][nodej] = 0
            visited.append((nodei,nodej))
            for di,dj in (1,0),(-1,0),(0,1),(0,-1):
                if 0 <= nodei+di < N and 0 <= nodej+dj < N:
                    if arr[nodei+di][nodej+dj] == 1:
                        stack.append((nodei+di,nodej+dj))
    cnt2.append(len(visited))


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
# print(arr)

cnt = 0
cnt2 = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt += 1
            dfs(i,j)

print(cnt)
cnt2.sort()
print(*cnt2, sep ='\n')