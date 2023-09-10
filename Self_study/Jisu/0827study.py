# IM 용 딱지놀이 백준

# 별 4, 원 3, 넴 2, 셈 1

N = int(input()) # 총 라운드 수
a = []
b = []
for _ in range(0,2*N,2):
    a.append(list(map(int, input().split()))) # for _ in range(0,2*N,2)] # 1라운드 첫번째 수가 카드 갯수 a[0]
    b.append(list(map(int, input().split()))) # for _ in range(1,2*N,2)] # 1라운드 첫번째 수가 카드 갯수 b[0]

for i in range(N):
    a[i].pop(0)
    b[i].pop(0)
    # print(i, a[i])
    # print(i, b[i])
    if a[i].count(4) > b[i].count(4):
        print('A')
    elif a[i].count(4) < b[i].count(4):
        print('B')
    elif a[i].count(4) == b[i].count(4):
        if a[i].count(3) > b[i].count(3):
            print('A')
        elif a[i].count(3) < b[i].count(3):
            print('B')
        elif a[i].count(3) == b[i].count(3):
            if a[i].count(2) > b[i].count(2):
                print('A')
            elif a[i].count(2) < b[i].count(2):
                print('B')
            elif a[i].count(2) == b[i].count(2):
                if a[i].count(1) > b[i].count(1):
                    print('A')
                elif a[i].count(1) < b[i].count(1):
                    print('B')
                elif a[i].count(1) == b[i].count(1):
                    print('D')