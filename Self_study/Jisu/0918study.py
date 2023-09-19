# 백준 재귀
# import sys
# input = sys.stdin.readlines

# def jaegui(N):
#     if N <= 1:
#         return N
#     else:
#         return jaegui(N-1) + jaegui(N-2) 

# N = int(input())
# print(jaegui(N))


N = int(input())
cnt = 2
result = [0]*(N+1)
result[0] = 0
result[1] = 1
while cnt <= N:
    # print(cnt)
    result[cnt] = result[cnt-1] + result[cnt-2]
    cnt += 1

print(result[N])