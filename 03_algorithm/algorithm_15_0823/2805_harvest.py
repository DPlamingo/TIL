# IM용 농작물 수확

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    origin_N = N//2

    sum_value = 0
    for i in range(N):
        if i <= origin_N:
            print(i)
            for j in range(origin_N-i, origin_N+1+i):
                print(j)
                sum_value += arr[i][j]
        else:
            for j in range(origin_N-N+i+1, origin_N+N-i):
                sum_value += arr[i][j]

    print(sum_value)