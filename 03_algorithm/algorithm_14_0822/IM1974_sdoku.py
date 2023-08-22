# IM 대비용 스도쿠

# 어차피 스도쿠 특성상 숫자합이 같아야함
# 1~9 까지 합 45이 범위에 다 되게 찾아본다.

T = int(input())
for tc in range(1, 1+T):
    sdoku = [list(map(int, input().split())) for _ in range(9)]

    sdoku_rev = [[0]*9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            sdoku_rev[i][j] = sdoku[j][i]

    cnt = 0
    for i in range(9):
        if sum(sdoku[i]) == 45:
            cnt += 1
        if sum(sdoku_rev[i]) == 45:
            cnt += 1

    delta = [[0,1],[0,0],[0,-1],[-1,-1],[-1,0],[-1,1],[1,-1],[1,0],[1,1]]
    list_sum = []
    for i in range(1,9,3):
        # print(i)
        for j in range(1,9,3):
            sum_value = 0
            for ki,kj in delta:
                sum_value += sdoku[i+ki][j+kj]
            list_sum.append(sum_value)

    for i in list_sum:
        if i == 45:
            cnt += 1

    if cnt == 27:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
