import sys
sys.stdin = open('input0803study.txt')


T, K = list(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(T)]

case = []
cnt = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        
        if arr[i] == arr[j]:
            case.append(arr[i])
            print(case)
        
            if arr[i].count(arr[j]) >= K:
                 
                print(cnt)
result = len(arr) - len(case) - a
print(result)