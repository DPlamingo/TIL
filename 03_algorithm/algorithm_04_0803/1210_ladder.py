import sys
sys.stdin = open('input1210.txt')

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    go = 0
    # print(arr)

    for j in range(100):

        while arr[go][j] != 2: # 2면 통과

                if arr[go][j] == True: # 현재 장소가 1이면 통과
                    if (arr[go-1][j] and arr[go+1][j]) != True :  #양 옆으로 확인
                        go += 1 # 양옆이 못가면 밑으로
                    elif arr[go-1][j] == True: # 좌측 이 있다면,
                        while arr[go-1][j] != True: # 좌측 계속 있다면 반복
                            j -= 1
                        if arr[go-1][j] != True: # 좌측 없다면 내려감
                            go += 1
                        continue
                    elif arr[go+1][j] == True:
                        while arr[go+1][j] != True:
                            j += 1
                        if arr[go+1][j] != True:
                            go += 1
                        continue


        print(f'#{tc} {j}')



