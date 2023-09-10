# 백준 브1 yangjojang of the year

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]
    # print(arr)

    list_name = []
    list_alchol = []
    for name, alchol in arr:
        list_name.append(name)
        list_alchol.append(int(alchol))

    print(list_name[list_alchol.index(max(list_alchol))])