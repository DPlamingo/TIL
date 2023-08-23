# Im 대비용, 최대 성적표 만들기

T = int(input())
for tc in range(1, 1+T):
    N, K = map(int, input().split())
    records = list(map(int, input().split()))

    sorted_records = sorted(records)
    total = 0
    for i in range(K):
        total += sorted_records.pop()

    print(f'#{tc} {total}')