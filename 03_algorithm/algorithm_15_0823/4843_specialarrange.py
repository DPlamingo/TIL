# IM 대비용 특별한정렬

T = int(input())
for tc in range(1, 1+T):
    N = int(input())

    arr = list(map(int, input().split()))

    queue = []
    for _ in range(5):
        queue.append(arr.pop(arr.index(max(arr))))
        queue.append(arr.pop(arr.index(min(arr))))

    print(f'#{tc}',*queue)