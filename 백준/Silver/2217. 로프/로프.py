# 2217.로프 백준 문제

N = int(input())
ropes = [0] * (N)
for i in range(N):
    ropes[i] = int(input())

max = 0

ropes.sort(reverse=True)
# print(ropes)
for i in range(len(ropes)):
    if max < ropes[i]*(i+1):
        max = ropes[i]*(i+1)

print(max)

