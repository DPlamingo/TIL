# IM 대비용 백준 직사각형

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    N = max(x1, y1, p1, q1, x2, y2, p2, q2)

    arr = [[0] * (N+1) for _ in range(N+1)]

    for i in range(y1, q1+1):
        for j in range(x1, p1+1):
            arr[i][j] += 1
    
    for i in range(y2, q2+1):
        for j in range(x2, p2+1):
            arr[i][j] += 1
   

    cnt = 0
    cnt2 = 0
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] == 2:
                cnt += 1
            if arr[i].count(2) > 1:
                cnt2 += 1
                 

    if cnt < 1:
        print('d')
    if cnt == 1:
        print('c')
    if cnt > 1:
        if cnt2 > 1:
            print('a')
        else:
            print('b')