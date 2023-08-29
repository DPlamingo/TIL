# IM 용 당근 포장하기

import sys
sys.stdin = open('input16811.txt')

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    carrets = list(map(int,input().split()))
    carrets.sort() # 당근 오름차순

    big = [    ] # 큰상자
    middle = [] # 중간상자
    small = [] # 작은상자
    if N%3 != 0:
        ditr = N//3 + 1
    else:
        ditr = N//3

    cnt2 = 0
    for i in carrets:
        if cnt2 >= 1 and i == carrets[cnt2-1]:
            pass
        else:
            cnt = carrets.count(i)
            for j in range(cnt):
                if len(small) < ditr:
                    small.append(carrets[cnt2])
                    # print(small,'s')
                    cnt2 += 1
                else:
                    if len(middle) < ditr:
                        middle.append(carrets[cnt2])
                        # print(middle,'m')
                        cnt2 += 1
                    else:
                        if len(big) < ditr:
                            big.append(carrets[cnt2])
                            # print(big,'b')
                            cnt2 += 1

    if len(small) + len(middle) + len(big) == N:
        result = max(len(small), len(middle), len(big)) - min(len(small), len(middle), len(big))
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} -1')

