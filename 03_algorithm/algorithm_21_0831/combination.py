# 조합

# idx : 이번 회차 조사 시작 지점
def comb(now, r, idx):
    if now == r:
        print(check[:r]) # r개 까지만 보여줘
    else:
        for i in range(idx, len(num)):
            check[now] = num[i]
            comb(now+1, r, i)
        
num = [1, 2, 3]
# 실제 조합에 구성되는 요소들을 담을 리스트
check = [0] * len(num)
comb(0, 2, 0)