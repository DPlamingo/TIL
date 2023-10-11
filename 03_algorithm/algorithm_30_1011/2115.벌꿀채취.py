# 2115. 벌꿀 채취

T = int(input())
for tc in range(1, 1+T):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]

    # 1차원 배열 하나 만들어서 허니들의 합을 쫙 배열함
    lst = []
    for i in range(N):
        for j in range(N-M):
            cnt = 0
            if sum(honey[i][j:j+M]) <= 13:
                for k in range(M):
                    cnt += honey[i][j+k]**2
                lst.append(cnt)
            else:
