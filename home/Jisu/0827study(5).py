# IM 용 백준 경비원

# 1 북, 2 남, 3 서, 4 동
# 1, 2 일경우 좌측에서 칸수
# 3, 4 일경우 위에서 칸수

x, y = map(int, input().split()) # 총배열 넓이
N = int(input()) # 상점 갯수
arr = [list(map(int, input().split())) for _ in range(N+1)]
# dong = list(map(int, input().split()))

list_str = []
for i, j in arr:
    if i == 1:
        list_str.append([0,j])
    elif i == 2:
        list_str.append([y,j])
    elif i == 3:
        list_str.append([j,0])
    else:
        list_str.append([j,x])

value = 0
for i, j in list_str:
    if abs(list_str[-1][0] - i) == y:
        value += min(abs(list_str[-1][1]+j-2*x),abs(list_str[-1][1]+j))+y
        
    elif abs(list_str[-1][1] - j) == x:
        value += min(abs(list_str[-1][0]+j-2*y),abs(list_str[-1][0]+i))+x
    else:
        value += abs((list_str[-1][0]-i)+(list_str[-1][1]-j))

print(value)