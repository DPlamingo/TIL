import sys
sys.stdin = open('input0804(2).txt')

T = int(input())
for tc in range(1, 1+T):
    M, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    id = [-1,1,0,0]
    jd = [0,0,-1,1]

    list_sum = []
    for i in range(M):
        for j in range(N):
            if 0 <= i+id[i] < M and 0 <= j+jd[j] < N:
                list_sum.append(arr[i+id[i]][j+jd[j]])

            print(list_sum)