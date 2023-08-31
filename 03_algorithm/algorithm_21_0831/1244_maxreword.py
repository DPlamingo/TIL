# 최대 상금 HW


def change(numbers, cnt, N):
    if cnt == int(N):
        print(int(''.join(numbers)))
    else:
        sort_numbers = sorted(numbers, reverse=True)
        if numbers[cnt] != sort_numbers[cnt]:
            numbers[numbers.index(sort_numbers[cnt])], numbers[cnt] = numbers[cnt], numbers[numbers.index(sort_numbers[cnt])]
            change(numbers, cnt + 1, N)

T = int(input())
for tc in range(1, T + 1):
    nums, N = map(str, input().split())
    list_nums = list(nums)
    change(list_nums, 0, N)

