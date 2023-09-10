# 풍선팡

import sys
sys.stdin = open('input0820study(3).txt')

T = int(input())
for tc in range(1, 1+T):
    M, N = map(int, input().split())
    balloons = [list(map(int, input().split())) for _ in range(M)]

    dl = [[1,0],[-1,0],[0,1],[0,-1]]

    list_balloons = []
    for i in range(M):
        for j in range(N):
            sum_balloons = balloons[i][j]
            for ki, kj in dl:
                for l in range(1,balloons[i][j]+1):
                    if 0 <= i+ki*l < M and 0 <= j+kj*l < N:
                        sum_balloons += balloons[i+ki*l][j+kj*l]
                        list_balloons.append(sum_balloons)
    max_balloons = max(list_balloons)
    print(f'#{tc} {max_balloons}')