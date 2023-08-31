# 화물 도크

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    worktime = [list(map(int, input().split())) for _ in range(N)]

    worktime.sort(key=lambda x:x[1]-x[0])
    # print(worktime,'worktime')
    worktable = [0] * 25
    cnt = 0
    for s, e in worktime:
        cnt += 1
        for i in range(s,e):
            worktable[i] += 1

        if worktable.count(2) > 0:
            cnt -= 1
            for j in range(s,e):
                worktable[j] -= 1


    print(cnt)