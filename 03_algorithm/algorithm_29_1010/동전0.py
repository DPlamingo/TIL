def divide(K):
    global cnt
    if K == 0:
        return

    for i in reversed(Ai):  # 큰 동전부터 사용하도록 변경
        div = K // i
        if div > 0:
            cnt += div
            K -= div * i

N, K = map(int, input().split())
Ai = [int(input()) for _ in range(N)]

cnt = 0
divide(K)
print(cnt)
