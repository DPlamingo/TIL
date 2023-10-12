# 1949. 등산로 조성

# 가로 세로 돌면서 작은거 계속 확인
# idea 각자리를 K만큼 빼서 등산로를 구해보고,
# 그 지도와 전체 지도에서 양 옆자리랑 비교했을때 차이


def dfs(i, j):
    stack = [(i,j)]
    visited = []
    while stack:
        nodei, nodej = stack.pop()
        for idx, idy in (1,0),(-1,0),(0,1),(0,-1):
            reali, realj = nodei+idx, nodej+idy
            if 0 <= reali < N and 0<= realj < N and maps[nodej][nodej] > maps[reali][realj] and (reali,realj) not in visited:
                visited.append((reali, realj))
                stack.append((reali, realj))


T = int(input())
for tc in range(1, 1+T):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    # dfs 각 자리마다 출발해서, 길이 큰값 저장
    memo = [[0]*N for _ in range(N)] # 맵에 0이 여러개
