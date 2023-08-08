import sys
sys.stdin = open('input1209.txt')


for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # print(arr)
    n = 100
    m = 100

    list_sum = []

    sum_left_slash = 0
    sum_right_slash = 0

    for i in range(n): # n은 행
        sum_row = 0
        for j in range(m): # m은 열
            sum_row += arr[i][j] # 행의 합
        list_sum.append(sum_row) # 행의 합 리스트

    for j in range(n):
        sum_column = 0
        for i in range(m):
            sum_column += arr[i][j] # 열의 합
        list_sum.append(sum_column) # 열의 합 리스트

    for i in range(n):
        sum_left_slash += arr[i][i] # 좌측 대각선의 합
        sum_right_slash += arr[i][n-1-i] # 우측 대각선의 합
    list_sum.append(sum_left_slash)
    list_sum.append(sum_right_slash)


    max_sum = max(list_sum)
    print(f'#{tc} {max_sum}')