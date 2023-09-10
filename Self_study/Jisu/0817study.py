# 색종이

T = int(input())
paper = [[0]*(1001) for _ in range(1001)]

for tc in range(1, 1+T):
    y, x, m, n = map(int, input().split())


    for i in range(y, y+m):
        for j in range(x, x+n):
            paper[i][j] = tc

for j in range(T):
    cnt = 0
    for i in range(1001):
        for k in range(1001):
            if paper[i][k] == j+1:
                cnt += 1
    
    
    print(cnt)    