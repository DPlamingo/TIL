import sys
sys.stdin = open('input0803.txt')

T = int(input())
for tc in range(1, 1+T):
    N, Q = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(Q)]

    list_box = [0] * (N) # 리스트 박스에 0공간을 채워 넣음

    for i in range(Q): # 몇회 값 변경할지

        for j in range(arr[i][0]-1, arr[i][1]): # 리스트 값에 있는 애들 범위지정

            list_box[j] = arr[i][0] # 리스트 자리에 대해 값 더해주고, 
                                    # 누적이 없으므로 따로 더 해줄건없음
    int_box = ' '.join(map(str, list_box))
    
    print(f'#{tc} {int_box}')