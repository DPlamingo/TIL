# 촌수계산

n = int(input()) # 전체 사람 수
chinchuc1, chinchuc2 = map(int, input().split())  # 두사람 번호
m = int(input()) # 부모 자식들간 관계 개수
connections = [list(map(int, input().split())) for _ in range(m)]
cnt = 0
visited = []
queue = []

dp = [[] for _ in range(n+1)]
for i, j in connections:
    if j not in dp[i]:
        dp[i].append(j)
    if i not in dp[j]:
        dp[j].append(i)

print(dp)

# 찾을때 까지 반복
def search(i):
    global cnt
    cnt += 1
    if chinchuc2 in dp[i]:
        print(cnt)
    else:
        visited.append(i)
        search(i)


#
# def bfs(start):
#     queue = [start]
#     visitied = []
#     while queue:
#         node = queue.pop(0)
#         if node not in visitied:
#             queue.append(node)
#             visitied.append(node)
#