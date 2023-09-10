import sys
sys.stdin = open('input0812.txt')

T = int(input())
for tc in range(1, 1+T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    
    cnt_num = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                # print(arr[i][j])
                cnt += 1
                if cnt == K and (j == N-1 or arr[i][j+1] == 0): # K가됬는데, 뒤에가 0이 되거나, 끝번호면 총괄 넘버를 올린다.
                    cnt_num += 1

            elif arr[i][j] == 0:
                cnt = 0
            
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                # print(arr[i][j])
                cnt += 1
                if cnt == K and (i == N-1 or arr[i+1][j] == 0): # K가됬는데, 뒤에가 0이 되거나, 끝번호면 총괄 넘버를 올린다.
                    cnt_num += 1

            elif arr[i][j] == 0:
                cnt = 0
    
    print(f'#{tc} {cnt_num}')