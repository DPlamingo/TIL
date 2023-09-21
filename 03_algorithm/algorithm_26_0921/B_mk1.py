# 1로 만들기

# x 가 3으로 나누어 떨어지면, 3으로 나눈다.
# x 가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

N = int(input())

dp = [0]*(N+1)

for i in range(2, N+1): # dp 각 인덱스가 값임
    dp[i] = dp[i-1]+1 # 1을 더한 값

    if i % 2 == 0: # 2의 배수와 cnt 확인
        dp[i] = min(dp[i], dp[i//2]+1)

    if i % 3 == 0: # 3의 배수와 cnt 확인
        dp[i] = min(dp[i], dp[i//3]+1)

result = dp[N]
print(result)