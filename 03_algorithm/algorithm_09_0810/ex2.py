import sys
sys.stdin = open('inputex2.txt')

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [1, 0, -1, 0, 0] # 하, 좌, 상, 우, 본인
    dj = [0, -1, 0, 1, 0]
    max_value = 0
    list_balloon = []

    for i in range(N):
        for j in range(M):
            sum_cal = 0
            for k in range(5):
                if 0 <= i+di[k] < N and 0 <= j+dj[k] < M:
                    sum_cal += arr[i+di[k]][j+dj[k]]
            list_balloon.append(sum_cal)


    result = max(list_balloon)
    print(f'#{tc} {result}')


    # print(arr)