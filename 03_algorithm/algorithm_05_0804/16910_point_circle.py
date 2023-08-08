import sys
sys.stdin = open('input16910.txt')

T = int(input())
for tc in range(1, T+1):
    arr = int(input())
    # print(arr)
    # print('ttttt')
    # 자, 시작은 특정 값을 받았을떄
    # 반지름은 N 이고 그에 대한 x,y값 구해야됨
    # 빈 리스트에 x,y 값 넣으면됨
    # 근데 - 값은 안넣어지니 양수의 x 2배하고
    # 0, 0 추가할 예정
    list_bean = []
    for i in range(-arr,arr+1):
        for j in range(-arr,arr+1):
            if (i**2) + (j**2) <= arr**2:
                list_bean.append([i, j])
    # print(list_bean)
    result = len(list_bean)
    print(f'#{tc} {result}')