# 백준 점프

# nxn 게임판에 수가 정해짐
# 가장 왼쪽 위에서 가장 오른쪽 아래로 점프함

# dp[i][j] > 0, arr[i][j] > 0 범위



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# dp 생성 및 초기값 설정
dp = [[0] * N for _ in range(N)]
dp[0][0]=1

for i in range(N):
    for j in range(N):
        # 경로 있고, 점프 숫자가 있는 경우
        if dp[i][j] > 0 and arr[i][j] > 0: 
            jump = arr[i][j]
            # 우측 범위 내에 있다면,
            if j+jump < N : 
                dp[i][j+jump] += dp[i][j]
            # 아래 범위내에 있다면,
            if i+jump < N : 
                dp[i+jump][j] += dp[i][j]

print(dp[N-1][N-1])
