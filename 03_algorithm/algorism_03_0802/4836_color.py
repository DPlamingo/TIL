import sys
sys.stdin = open('input4836.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    # color = 1 (빨강)
    # color = 2 (파랑)

    table_10 = [[0]*10 for _ in range(10)]

    # print((table_10))

    for i in arr: # 영역 리스트를 뽑음
        for j in range(i[0], i[2] + 1):  # 행 범위는 리스트의 [2] - [0] 고정임,                                          
            for k in range(i[1], i[3] + 1): # 열 범위는 리스트의 [3] - [1] 고정
                table_10[j][k] += i[4]
                # if i[4] == 1:  # Color = 1 (빨강) [4]는 색상 고정임
                #     table_10[j][k] += 1
                # else:  # Color = 2 (파랑)
                #     table_10[j][k] += 2

    # print(table_10_1)
    # print(table_10_2)
    count_color = 0
    for i in range(10): # table_10을 뒤짐
        for j in range(10):
            if table_10[i][j] == 3: # 보라색은 3이기에 3 갯수만 셈
                count_color += 1

    print(f'#{tc} {count_color}')


