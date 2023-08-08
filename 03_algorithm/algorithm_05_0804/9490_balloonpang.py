import sys
sys.stdin = open('input16268.txt')

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# 우 하 좌 상

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j] # 터트린 풍선의 꽃가루 수
            for k in range(4): # i, j 인접에 대해
                for p in range(1, arr[i][j]+1):
                    ni, nj = i+di[k]*p, j+dj[k]*p
                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += arr[ni][nj] # 주변칸 풍선의 꽃가루 수

            if max_v < cnt:
                max_v = cnt
    print(f'#{tc} {max_v}')
