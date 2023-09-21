# 백준 2xn 타일링 2

# 규칙성을 먼저 찾아야한다.
# 각 경우의 수는 지나온 경우의 수 1번째 인덱스 + 1 + 2번째 인덱스의 2배


N = int(input())
dp = [0]*(N+1)
dp[1], dp[2] = 1, 3 # 초기설정

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]*2


ans = dp[N]
print(ans%10007)


