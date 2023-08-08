import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # print(arr)

# min_m_value = 0
    max_M = []
# max_m_value = 0
    for i in range(N-M+1):
        max_list = 0
        for j in range(i, i+M):
            max_list = max_list + arr[j]
        max_M.append(max_list)
        # print(max_M)


    result = max(max_M) - min(max_M)

    print(f'#{tc} {result}')

# T = int(input())
#
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     min_M = []
#     max_M = []
#
#     for i in range(N - M + 1):
#         min_M.append(sum(arr[i:i + M]))  # Calculate the sum of subarray of length M and store in min_M
#
#     for i in range(N - M + 1):
#         max_M.append(sum(arr[i:i + M]))  # Calculate the sum of subarray of length M and store in max_M
#
#     min_sum = min(min_M)  # Find the minimum sum from min_M
#     max_sum = max(max_M)  # Find the maximum sum from max_M
#
#     result = max_sum - min_sum
#
#     print(f'#{tc+1} {result}')
numbers = [1, 3, 4, 5, 7]
print(sum(numbers[1:3]))