# IM 용 백준 경비원

# 1 북, 2 남, 3 서, 4 동
# 1, 2 일경우 좌측에서 칸수
# 3, 4 일경우 위에서 칸수

x, y = map(int, input().split()) # 총배열 넓이
N = int(input()) # 상점 갯수
arr = [list(map(int, input().split())) for _ in range(N)]
dong = list(map(int, input().split())) # 동근이 위치

value = 0
if dong[0] == 1:
# 2 고정일때만 생각해봄
    for side, dist in arr: # 방향과 거리
        if side == 2: # 동근이 반대 방향
            if dist >= dong[1]: # 동근이 위치보다 작다면 시계가 빠름
                value += abs((x-dist)+(x-dong[1]+y))

            else: # 동근이 위치보다 크다면 반시계
                value += abs(dist+dong[1]+y)
    
        if side == 1: # 동근이랑 방향이 같으면
            value += abs(dist-dong[1])

        if side == 4: # 동근이 왼쪽 방향이라면
            value += abs(dong[1]+(y-dist))

        if side == 3: # 동근이 오른쪽 이라면
            value += abs((x-dong[1])+(y-dist))



if dong[0] == 2:
# 2 고정일때만 생각해봄
    for side, dist in arr: # 방향과 거리
        if side == 1: # 동근이 반대 방향
            if dist >= dong[1]: # 동근이 위치보다 작다면 시계가 빠름
                value += abs(dist+dong[1]+y)
            else: # 동근이 위치보다 크다면 반시계
                value += abs((x-dist)+(x-dong[1]+y))
    
        if side == 2: # 동근이랑 방향이 같으면
            value += abs(dist-dong[1])

        if side == 3: # 동근이 왼쪽 방향이라면
            value += abs(dong[1]+(y-dist))

        if side == 4: # 동근이 오른쪽 이라면
            value += abs((x-dong[1])+(y-dist))

if dong[0] == 3:
# 2 고정일때만 생각해봄
    for side, dist in arr: # 방향과 거리
        if side == 4: # 동근이 반대 방향
            if dist >= dong[1]: # 동근이 위치보다 작다면 시계가 빠름
                value += abs((x-dist)+(x-dong[1]+y))
            else: # 동근이 위치보다 크다면 반시계
                value += abs(dist+dong[1]+y)
    
        if side == 3: # 동근이랑 방향이 같으면
            value += abs(dist-dong[1])

        if side == 1: # 동근이 왼쪽 방향이라면
            value += abs(dong[1]+(dist))

        if side == 2: # 동근이 오른쪽 이라면
            value += abs((y-dong[1])+(dist))

if dong[0] == 4:
# 2 고정일때만 생각해봄
    for side, dist in arr: # 방향과 거리
        if side == 3: # 동근이 반대 방향
            if dist >= dong[1]: # 동근이 위치보다 작다면 시계가 빠름
                value += abs(dist+dong[1]+y)
            else: # 동근이 위치보다 크다면 반시계
                value += abs((x-dist)+(x-dong[1]+y))
    
        if side == 4: # 동근이랑 방향이 같으면
            value += abs(dist-dong[1])

        if side == 2: # 동근이 왼쪽 방향이라면
            value += abs(dong[1]+(y-dist))

        if side == 1: # 동근이 오른쪽 이라면
            value += abs((x-dong[1])+(y-dist))

print(value)