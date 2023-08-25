# IM 용 자리배치기

C, R = map(int, input().split())
customer = int(input())

arr = [[0] *C for _ in range(R)]


cnt = 0
i = R-1
j = 0
while cnt != C*R+1:
    cnt += 1
    arr[i][j] = cnt
    if i > 0 and arr[i-1][j] == 0:
        i -= 1
    elif j < C-1 and arr[i][j+1] == 0:
        j += 1
    elif i < R-1 and arr[i+1][j] == 0:
        i += 1
    elif j > 0 and arr[i][j-1] == 0:
        j -= 1
print(arr)

