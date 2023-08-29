# N개의 물건
# 각 물건의 무게 W
# 가치 V
# 가치의 최대값은?
# 배낭의 총 무게제한 K
N, K = map(int, input().split())  # 물품수, 버틸수있는 무게
# 걍 무게 합 되기 전 최대값
arr = [list(map(int, input().split())) for _ in range(N)]
W = []
V = []
for w,v in arr:
    W.append(w)
    V.append(v)


list_check = []
for i in range(1 << N):
    check = []
    count = 0
    for j in range(N):
        if i & (1 << j):
            count += W[j]
            if count <= K:
                check.append(W[j])
    list_check.append(check)


result = []
for i in range(len(list_check)):
    cnt = 0
    for j in range(len(list_check[i])):
        cnt += V[W.index(list_check[i][j])]
    result.append(cnt)

result.sort()
print(result[-1])