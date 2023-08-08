import sys
sys.stdin = open('input16268.txt')

di = [0, 1, 0, -1] 
dj = [1, 0, -1, 0]
# 우 하 좌 상

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0 #
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j] # 터트린 풍선의 꽃가루 수
            for k in range(4): # i,j 인접에 대해
                ni, nj = i+di[k], j+dj[k] # 위치
                if 0<=ni<N and 0<=nj<M:
                    cnt += arr[ni][nj] # 주변애들이 나왔을때 값을 더함
            if max_v < cnt: # i, j 인접 풍선까지 더하고 나면
                max_v = cnt
    print(f'#{tc} {max_v}') # 모든 위치에서 확인이 끝나면