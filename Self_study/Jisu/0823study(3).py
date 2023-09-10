T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # print(arr)
    mid = N//2
    # print(mid)
    sum_arr = 0
    for i in range(N):
        if i <= mid:
            # print(i)
            for j in range(mid-i,mid+1+i):
                # print(j,'j')
                sum_arr += arr[i][j]
                # print(sum_arr,'sum')
        elif i > mid:
            for j in range(mid+1-N+i,mid+N-i):
                sum_arr += arr[i][j]
    print(f'#{tc} {sum_arr}')