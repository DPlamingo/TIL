# 미로의 거리
import sys
sys.stdin = open('input5105.txt')


def bfs(sti, stj, N):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((sti, stj)) # 시작점 인큐
    visited[sti][stj] = 1 # 시작점 인큐표시
    while q:    # 큐가 비워질 때 까지
        i, j = q.pop(0) # 디큐
        if maze[i][j] == 3:
            return visited[i][j]-2 # 지나온 칸 수 리턴
        # 인접하고 인큐된 적 없으면
        # 인큐, 인큐표시
        for di, dj in [[0,1], [1,0],[0,-1],[-1,0]]:
            ni,nj =i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j]+1
    return 0 # 3인칸에 도달 할 수 없는 경우.


def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = find_start(N)
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')
