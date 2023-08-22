# IM 대비용 두개의 숫자열

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    Ai = list(map(int,input().split()))
    Bj = list(map(int,input().split()))
    list_sum = []
    # 길이를 비교하고 더큰 길이의 범위안에서 리스트가 움직인다.
    if N > M:
        for i in range(N-M+1):
            C = [0] * N
            for j in range(M):
                C[i+j] = Bj[j]

            sum_result = 0
            for k in range(N):
                result = C[k] * Ai[k]
                sum_result += result

            list_sum.append(sum_result)
        print(f'#{tc} {max(list_sum)}')
    else:
        for i in range(M - N + 1):
            C = [0] * M
            for j in range(N):
                C[i + j] = Ai[j]

            sum_result = 0
            for k in range(M):
                # print(C[k], Bj[k])
                result = C[k] * Bj[k]
                sum_result += result

            list_sum.append(sum_result)
        print(f'#{tc} {max(list_sum)}')
