# 숫자회전

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    ro_90 = [[0]*N for _ in range(N)]
    ro_180 = [[0]*N for _ in range(N)]
    ro_270 = [[0]*N for _ in range(N)]

    # 90도면 00 01 02 가 02 12 22 가됨됨
        #   02 12 22 가 22 21 20 가 됨
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            ro_90[j][N-i-1] = arr[i][j]

    for i in range(N):
        for j in range(N):
            ro_180[j][N-i-1] = ro_90[i][j]

    for i in range(N):
        for j in range(N):
            ro_270[j][N - i - 1] = ro_180[i][j]

    for i in range(N):
        print(f'{"".join(map(str,ro_90[i]))} {"".join(map(str,ro_180[i]))} {"".join(map(str,ro_270[i]))}')
    print()