# IM 대비용 파리퇴치3

import sys
sys.stdin = open('input12712.txt')

T = int(input())  # tc 케이스 개수
for tc in range(1, 1+T):
    N,M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    deltaplus = [[1,0],[-1,0],[0,1],[0,-1]]
    deltax = [[1,1],[1,-1],[-1,-1],[-1,1]]

    list_value = []
    for i in range(N):
        for j in range(N):
            sum_valueplus = arr[i][j]
            sum_valuex = arr[i][j]
            for k in range(4):
                for l in range(1,M):
                    yplus = i + deltaplus[k][0]*l
                    xplus = j + deltaplus[k][1]*l
                    yx = i + deltax[k][0]*l
                    xx = j + deltax[k][1]*l
                    if 0 <= yplus < N and 0 <= xplus < N:
                        sum_valueplus += arr[yplus][xplus]
                    if 0 <= yx < N and 0 <= xx < N:
                        sum_valuex += arr[yx][xx]

            list_value.append(sum_valueplus)
            list_value.append(sum_valuex)

    print(f'#{tc} {max(list_value)}')