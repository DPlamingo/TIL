# 색종이 2 집에서

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

white_paper = [[0]*100 for _ in range(100)]

# print(white_paper)

for i in range(N):
    for j in range(arr[i][1],arr[i][1]+10):
        for k in range(arr[i][0],arr[i][0]+10):
            white_paper[j][k] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if white_paper[i][j]:
            cnt += 1

print(cnt)