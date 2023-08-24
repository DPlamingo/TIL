# IM 용 주사위 쌓기(백준)

# (A,F) (B,D) (C,E)
# (0,5) (1,3) (2,4)

N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
dices1 = list(dices)
dices2 = list(dices1)
dices3 = list(dices2)

# A, F 제거
max_value_AF = 0
max_value_BD = 0
max_value_CE = 0

for i in range(N):
    dices1[i].pop(0) # A 번 인덱스
    dices1[i].pop(4) # 한번 자리 밀림 F인덱스
    dices2[i].pop(1) # B 번 인덱스
    dices2[i].pop(2) # D 번 인덱스
    dices3[i].pop(2) # C 번 인덱스
    dices3[i].pop(3) # E 번 인덱스
    max_value_AF += max(dices1)
    max_value_BD += max(dices2)
    max_value_CE += max(dices3)

result = max(dices1,dices2,dices3)
print(result)