# IM 대비용

import sys
sys.stdin = open('input1208.txt')

tc = 0
while True:
    tc += 1
    try:
        N = int(input())
        arr = list(map(int, input().split()))

        for i in range(N):
            arr[arr.index(max(arr))] -= 1
            arr[arr.index(min(arr))] += 1

        result = max(arr) - min(arr)
        print(f'#{tc} {result}')


    except EOFError:
        break