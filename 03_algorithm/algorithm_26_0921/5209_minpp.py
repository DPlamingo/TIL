# 최소 생산 비용

# N종의 제품을 N곳 공장에서 한곳당 한가지씩 생산하려고한다.

# 2차원 행렬에서 같은 행 열로 구성되면 안된다.

# 최소 비용을 출력한다.
def backtracking(n, sum):
    global ans
    if ans < sum:
        return

    if n == N:
        ans = min(ans, sum)
        return

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1 # 방문 표시를 한다음에
            backtracking(n+1, graph[n][j] + sum) # 다음꺼, 합친거 보고
            visited[j] = 0 # 방문표시 돌린다.


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    ans = 100*N # 큰값
    visited = [0]*N

    backtracking(0, 0) # 합
    print(f'#{tc} {ans}')


