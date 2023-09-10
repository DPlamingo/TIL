# 줄세우기

import sys
sys.stdin = open('input0811.txt')

N = int(input())
arr = list(map(int, input().split()))

list_children = [0] * N
print(list_children)
for i in range(N):
    if list_children[N-1-arr[i]] == 0:
        list_children[N-1-arr[i]] = i+1

    elif list_children[N-1-arr[i]] != 0:
        for j in range(N-2-arr[i]):
            print(j)
            list_children[N-2-arr[i]-j] = list_children[N-1-arr[i]-j] # j= 0, i= 1 , N-1 = 4
            list_children[N-1-arr[i]-j] = i+1
    print(list_children)

print(list_children)  
