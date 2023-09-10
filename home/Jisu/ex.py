x, y = map(int, input().split())  # 블록의 가로 및 세로 길이
N = int(input())  # 상점의 개수
shops = [list(map(int, input().split())) for _ in range(N)]
dong_x, dong_y = map(int, input().split())  # 동근이의 위치

total_distance = 0

# 서쪽 또는 동쪽에 있는 경우
if dong_x in {3, 4}:
    for i, j in shops:
        if i in {3, 4}:
            total_distance += abs(dong_y - j)  # 둥근이와 상점의 y 좌표 차이
        elif i == 1:  # 북쪽에 있는 상점
            total_distance += j + dong_y  # 둥근이와 상점의 y 좌표 합
        else:  # 남쪽에 있는 상점
            total_distance += y - j + dong_y  # 둥근이와 상점의 y 좌표 차이와 블록의 세로 길이를 합함

# 북쪽 또는 남쪽에 있는 경우
else:
    for i, j in shops:
        if i in {1, 2}:
            total_distance += abs(dong_x - i)  # 둥근이와 상점의 x 좌표 차이
        elif i == 3:  # 서쪽에 있는 상점
            total_distance += x - j + dong_x  # 둥근이와 상점의 x 좌표 차이와 블록의 가로 길이를 합함
        else:  # 동쪽에 있는 상점
            total_distance += j + dong_x  # 둥근이와 상점의 x 좌표 합

print(total_distance)
