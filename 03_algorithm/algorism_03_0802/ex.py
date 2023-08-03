import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    print(arr)
    counting_arr = [0] * 10
    print(counting_arr)

    for num in arr:
        counting_arr[num] += 1
    print(counting_arr)
    result = 0
    num = 0
    for index in range(len(counting_arr)):
        if counting_arr[index] >= result:
            result = counting_arr[index]
            num = index
    print(f'#{tc} {num} {result}')