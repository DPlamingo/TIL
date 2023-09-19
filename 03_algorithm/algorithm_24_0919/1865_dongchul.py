# 똥 처리...

def max_success(N, worker):
    # dp[i][mask]: i번째 일까지 진행하고, mask에 포함된 직원들에게 일을 배정했을 때
    # 얻을 수 있는 최대 성공 확률
    dp = [[0] * (1 << N) for _ in range(N)]

    # 초기값 설정: 첫 번째 일을 배정한 경우
    for i in range(N):
        dp[0][1 << i] = worker[i][0]

    # 모든 일을 배정하는 경우를 고려
    for i in range(1, N):
        for mask in range(1 << N):
            for j in range(N):
                if mask & (1 << j) == 0:  # j번 직원에게 아직 일을 배정하지 않은 경우
                    dp[i][mask | (1 << j)] = max(dp[i][mask | (1 << j)], dp[i - 1][mask] * worker[j][i] / 100)

    # 모든 직원에게 일을 배정한 경우 중 최대 성공 확률 찾기
    max_probability = 0
    for mask in range(1 << N):
        max_probability = max(max_probability, dp[N - 1][mask])

    return max_probability * 100


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    worker = [list(map(int, input().split())) for _ in range(N)]

    result = max_success(N, worker)/100
    print(f"#{tc} {result:.6f}")
