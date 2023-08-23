# IM 대비용, 민석이의 과제 체크하기

T = int(input())
for tc in range(1, 1+T):
    N, K = map(int, input().split())
    attendees = list(map(int, input().split()))

    attendance = list(range(1, 1+N))
    # print(attendance)
    for i in attendees:
        attendance.pop(attendance.index(i))
        # print(attendance)
    print(f'#{tc}',end=' ')
    for i in attendance:
        print(i,end=' ')
    print()
