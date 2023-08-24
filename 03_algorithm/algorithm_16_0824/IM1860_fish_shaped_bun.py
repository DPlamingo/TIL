# IM 용 진기의 최고급 붕어빵
import sys
sys.stdin = open('input1860.txt')

T = int(input())
for tc in range(1, 1+T):
    N, M, K = map(int, input().split())
    arrive = list(map(int, input().split()))

    time = -1
    bun = 0
    client = 0
    shutdown = ['master']
    while shutdown: # 장사중
        time += 1 # 시간초가 감
        if time != 0:
            if time % M == 0: # 사장님 속도
                bun += K # 빵 나옴

        for i in arrive: # 도착했나?
            if time == i: # 도착했으면
                client += 1 # 사람수 적고
                if bun - 1 >= 0: # 시간에 빵잇나?
                    bun -= 1 # 빵있으면, 팔고 빵 줄이기

                else: # 빵없으면
                    print(f'#{tc} Impossible') # 빵없어서 문다당요.
                    shutdown.pop() # 퇴근
                    break

        if time == max(arrive) and shutdown: # 마지막 손님왔을때까지 장사됬으면,
            print(f'#{tc} Possible')
            shutdown.pop()  # 퇴근
            break