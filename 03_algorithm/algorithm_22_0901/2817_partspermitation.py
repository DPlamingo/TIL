# 부분 수열의 합

T = int(input())
for tc in range(1, 1+T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    cnt2 = 0
    for i in range(1<<N):
        cnt = 0
        for j in range(N):
            if i & (1<<j):
                cnt += A[j]
        if cnt == K:
            cnt2 += 1

    print(f'#{tc} {cnt2}')