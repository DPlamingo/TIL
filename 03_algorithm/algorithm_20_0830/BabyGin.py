# BabyGin problem

# row : 현재 조사 대상
# chosen : 선택 대상
# 완전 검색을 할거다
    # 모든 N개의 원소를 다 조사 했는지 판단
def perm(row, chosen):
    global results
    if row == N:
        tmp =[]
        for i in chosen:
            tmp.append(data[i])
        results.append(tmp)
        return

    # 모든 N개의 원소를 조사 했는지 판단
    for i in range(N):
        # i번째 쓰겠다고 이전에 판정된 적이 있따면,
        # 현재 조사 대상을 i번째에 쓸 수 없으므로
        if i in chosen:
            continue
        chosen[row] = i # row번째 대상을 i번째에 둬서 사용하겠다.
        perm(row+1, chosen)
        chosen[row] = -1

for t in range(1, 5):
    N = 6
    data = input()
    results = []
    # i번째에 들어 갈 수 있는 수 0, N-1 까지를 제외한
    chosen = [-1] * N
    perm(0, )