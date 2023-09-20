def dfs(n, m):
    global ans
    if ans >= m:
        return

    if n == N:
        ans = max(ans, m)

    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            print(arr[n][j])
            dfs(n + 1, m * arr[n][j])
            v[j] = 0
            print(v)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = (-100) * N # 비교용
    v = [0] * (N) # 체크용, 방문 체크
    dfs(0, 1) # n : dfs 순서, m : 곱하기
    print(f'#{test_case} {ans}')
    # print(f'#{test_case} {f"{100 * (ans / (100 ** N)):.6f}"}')