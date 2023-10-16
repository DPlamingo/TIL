# 11399.ATM 백준 실버4

N = int(input())
Pi = list(map(int, input().split()))

# 최소인 방법은
# 오름차순으로 시작해서
# 쭉 곱해주면됨

Pi.sort()
result = 0
for i in range(N):
    result += Pi[i] * (N-i)

print(result)