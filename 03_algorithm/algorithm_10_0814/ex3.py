arr = list(range(1,11)) # 1~10
n = len(arr) # 길이가 10인 경우의 모든 수

for i in range(1<<10):
    subset = []
    for j in range(n):
        # i번째 경우의 수 일 때,
        # j번째 요소를 쓰니 마니?
        if i & (1 << j):
            subset.append(arr[j])
    # 부분집합의 합이 10이냐
    if sum(subset) == 10:
        print(subset)

