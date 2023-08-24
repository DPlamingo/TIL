# IM 대비용 정곤이읭 단조

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    A = list(map(int, input().split()))

    mult = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            mult.append(str(A[i] * A[j]))

    def check(arr):
        list_check = []
        for i in arr:
            for j in range(len(i)-1):
                if int(i[j]) > int(i[j+1]):
                    return False
                list_check.append(i)
                return list_check

    result = check(mult)
    if result:
        print(f'#{tc} {max(result)}')
    else:
        print(f'#{tc} -1')