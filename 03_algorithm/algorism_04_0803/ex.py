

arr = [8, 1, -4]

count_sum = 0
N = len(arr)
list_sum = []
for i in range(1<<N):
    sum_stor = []
    for j in range(N):
        if i & (1<<j):
            sum_stor.append(arr[j])
            # print((sum_stor))
            # print('...')
    # print(sum_stor)
    # print(',,,,')
print(sum_stor)
#     if sum(sum_stor) == 0 and len(sum_stor) != 0:
#         count_sum += 1
#         list_sum.append(sum_stor)
#
# print(list_sum)
# print(count_sum)
