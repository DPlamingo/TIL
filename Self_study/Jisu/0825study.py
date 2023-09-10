# 홈방범 서비스
import sys
sys.stdin = open('input0825.txt')


T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for K in range(1,N+1):
        price = K*K +(K-1)*(K-1)
        # 마름모
        angle = [[0]*(2*K-1) for _ in range(2*K-1)]

        for i in range(2*K-1):
            if i < K:
                for j in range(i+1):
                    angle[i][K-1-j] = 2
                    angle[i][K-1+j] = 2
            else:
                for j in range(K-i+3):
                    angle[i][K-1-j] = 2
                    angle[i][K-1+j] = 2

        frame = angle + arr

        print(angle)



                # i = 4, K-1에서 j는
        house = 0
        result = house * M - price
        if result > 0:
            print(house)
