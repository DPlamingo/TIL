# 자기 방으로 돌아가기
import sys
sys.stdin = open('input4408.txt')

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    list_rooms = [0] * 200 # 방 최대 크기
    # print(list_rooms1)
    for other, origin in rooms: # 복도 구간겹치면 시간이 그만큼 지체되는거 아님?
        if other % 2 == 0: # 짝수
            other_arr = other // 2 - 1 # 인덱스 지정
        else: # 홀수
            other_arr = other // 2 # 인덱스 지정
        if origin % 2 == 0:
            origin_arr = origin // 2 - 1
        else:
            origin_arr = origin // 2

        if other_arr > origin_arr:
            other_arr, origin_arr = origin_arr, other_arr
        for i in range(other_arr,origin_arr+1): # 인덱스가 겹치면 방에 기록
            list_rooms[i] += 1

    print(f'#{tc} {max(list_rooms)}')
