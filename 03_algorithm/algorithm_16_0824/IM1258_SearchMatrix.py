# IM 용 행렬찾기

import sys
sys.stdin = open('input1258.txt')

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    delta = [[1,0],[-1,0],[0,1],[0,-1],]

    cnt = 0
    for i in range(N):
        for j in range(N):
            for ki,kj in delta:
                if 0<= i+ki <N and 0<= j+kj <N:
                    arr[]
