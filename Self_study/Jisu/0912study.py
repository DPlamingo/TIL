# 백준 실2 DFS
import sys
sys.stdin = open('input0912.txt')


T = int(input())
for _ in range(1, 1+T):
    M, N, K = map(int, input().split())
    # M 가로, N 세로, K 배추 개수
    positions = [list(map(int, input().split())) for _ in range(K)]
    # print(positions)
    area = [[0]*M for _ in range(N)]
    for y,x in positions:
        # print(y,x)
        area[x][y] = 1
    
    delta = [[0,1],[1,0],[0,-1],[-1,0]]


    stack = []
    cnt = 0
    for i in range(N):
        for j in range(M):
            if area[i][j] == 1:
                stack.append((i,j))
                area[i][j] = 0
                cnt += 1
                while stack:
                    yi, xj = stack.pop()
                    for ky, kx in delta:
                        if 0 <= yi+ky < N and 0 <= xj+kx < M:
                            if area[yi+ky][xj+kx] == 1:
                                stack.append((yi+ky,xj+kx))
                                area[yi+ky][xj+kx] = 0
    
    print(cnt)