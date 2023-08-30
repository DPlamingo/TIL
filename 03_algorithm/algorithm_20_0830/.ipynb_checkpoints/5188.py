# 5188 최소합
import math

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    delta = [[1,0],[0,1]]

    check2 = [[] for _ in range(2*N-1)]

    print(check2)
    for i in range(N):
        for j in range(N):
            check2[i+j].append(arr[i][j])

    # print(check2)
    check4 = []
    check4.append(check2[0])


    for _ in range(len(check2)-1):
        check4.append([])
    # print(check4,'check4')
    # check4 = [[] for _ in range(2*N-1)]
    for i in range(len(check2)-1):

        for j in range(len(check2[i])):
            for k in range(len(check2[i+1])):
                cnt = check4[i][j]+check2[i+1][k]
                check4[i+1].append(cnt)
                # print(check2)

        # print(check2)
    print(f'#{tc} {max(check4[-1])}')