# IM용 수열

N, K = map(int, input().split())
temp = list(map(int, input().split()))
# print(temp)

# temp.sort()
# print(temp)
list_temp = [0] * (N+1)
for i in range(N):
    list_temp[i+1] = list_temp[i] + temp[i]

# print(list_temp)
result = []
for i in range(K,N+1):
    result.append(list_temp[i]-list_temp[i-K])

print(max(result))