# IM 대비용 고대석판

import sys
sys.stdin = open('input9489.txt')

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    check = []
    for i in range(N):
        cntx = 0
        for j in range(M):
            if arr[i][j] == 1:
                cntx += 1
                if j == M-1 or arr[i][j+1] == 0:
                    check.append(cntx)
                    cntx = 0


    for j in range(M):
        cnty = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnty += 1
                if i == N - 1 or arr[i+1][j] == 0:
                    check.append(cnty)
                    cnty = 0

    check.sort()
    print(f'#{tc} {check[-1]}')