import sys
sys.stdin = open('input0811(2).txt')

arr = [list(map(int, input().split())) for _ in range(4)]


list_sol = [[0]*8]*8
print(list_sol)
for i in range(4):
    for j in range(arr[i][0],arr[i][2]+1):
        for k in range(arr[i][1],arr[i][3]+1):
            
            list_sol[k][j] += 1

print(list_sol)

