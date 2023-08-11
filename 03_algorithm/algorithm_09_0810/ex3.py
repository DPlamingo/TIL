import sys
sys.stdin = open('inputex3.txt')

di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(M):
            value = arr[i][j]

            for kk in range(1, arr[i][j]+1):
                for k in range(4):
                    ni, nj = i + (di[k] * kk), j + (dj[k] * kk)

                    if 0 <= ni < N and 0 <= nj < M:
                        value += arr[ni][nj]

            result = max(result, value)
    print(f'#{tc} {result}')