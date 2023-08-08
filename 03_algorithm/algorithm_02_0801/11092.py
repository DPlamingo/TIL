T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
'''
3
5
1 1 2 3 3
10
3 10 5 5 8 3 9 1 3 3 
20
4 1 6 7 9 4 1 4 8 4 1 6 5 3 1 4 3 1 10 10 

'''

min_idx = 0
max_idx = 0
for i in range(1, N):
    if arr[min_idx] > arr[i]:
        min_idx = arr[i]
    if arr[max_idx] <= arr[i]:
        max_idx = arr[i]
ans = max_idx - min_idx
if ans < 0:
    ans *= -1

print(f'#{ans} {}')
# print(ans)
# abs(max_idx-min_idx)
# max(max_idx, min_idx) - min(max_idx, min_idx)