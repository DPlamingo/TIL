# IM용 러시아 국기같은 깃발

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    cnt = 0
    for i in arr:
        for j in range(N):
            if j == 0:
               cnt += i.count('R' or 'B')
            elif j == N-1:
                cnt += i.count('W' or 'B')

            for k in range(1,N-1):
                cnt += i.count()

    for i in range(1,N-1):
        for j in range()


    print(arr)