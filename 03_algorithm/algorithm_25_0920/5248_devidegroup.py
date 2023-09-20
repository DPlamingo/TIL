# 그룹나누기

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int,input().split())

    arr = list(map(int, input().split()))
    idx = [[] for _ in range(N+1)]


    for i in range(1,1+N):
        if i not in arr:
            idx[i].append(i)

    graph = []
    while arr:
        sub = []
        for i in range(2):
            sub.append(arr.pop(0))
        graph.append(sub)

    graph.sort(key=lambda x:(x[0]))
    for i in graph:
        i.sort()

    # print(idx)
    for index, value in graph:
        idx[index].append(value)

    print(idx)

    cnt = 0
    for i in idx:
        if i:
           cnt += 1
    print(cnt)