# IM용 magnetic

import sys
sys.stdin = open('input1220.txt')

tc = 0
while True:
    tc += 1
    try:
        N = int(input())
        arr = [list(map(int, input().split())) for _ in range(N)]


        for _ in range(N): # 배열만큼만함
            for i in range(N):
                for j in range(N):
                    if arr[i][j] == 1:
                        if i+1 < 100 and arr[i+1][j] == 0:
                            arr[i+1][j] = 1
                    elif arr[i][j] == 2:
                        if i-1 > 0 and arr[i-1][j] == 0:
                            arr[i-2][j] = 2
        cnt = 0
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 1:
                    if i+1 < N and arr[i+1][j] == 2:
                        cnt += 1

        print(f'#{tc} {cnt}')


    except EOFError:
        break