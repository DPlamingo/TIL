import sys
sys.stdin = open('input4837.txt')


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    sum_case = []
    N = len(A)
    count_case = 0
    for i in range(1<<N):
        list_sum = []
        for j in range(N):
            if i & (1<<j):
                list_sum.append(A[j])
                print(list_sum)

        if sum(list_sum) == arr[1] and len(list_sum) != 0 and len(list_sum) == arr[0]:
            # sum_case.append(list_sum)
            count_case += 1

    print(f'#{tc} {count_case}')