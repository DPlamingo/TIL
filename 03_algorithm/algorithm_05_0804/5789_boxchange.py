import sys
sys.stdin = open('input5789.txt')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(Q)]
    print(arr)
    list_box = [0] * (N+1)
    for i in range(Q):
        for j in range(2):
            list_box = arr[i][j]