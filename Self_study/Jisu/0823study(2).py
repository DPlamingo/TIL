import sys
sys.stdin = open('input0823.txt')

T = int(input())
for tc in range(1, 1+T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                for k in range(i,i+K):

                    
