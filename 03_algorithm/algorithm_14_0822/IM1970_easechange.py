# IM 대비 쉬운 거스름돈

# 돈의 개수를 세라
# easy

T = int(input())
for tc in range(1, 1+T):
    N = int(input())

    # 인덱스가 원
    cash = {50000:0, 10000:0, 5000:0, 1000:0,500:0,100:0,50:0,10:0}
    cash_key = [50000,10000,5000,1000,500,100,50,10]
    # def cash_fun(N):
    for i in cash_key:
        if N//i > 0:
            cash[i] += N//i
            N = N % i
            # cash_fun(N)
    print(f'#{tc}')
    for i in cash_key:
        print(cash[i], end=' ')
    print()