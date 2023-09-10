# IM 대비용 백준 직사각형

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # 두 직사각형의 겹치는 부분을 파악합니다.
    if p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        print('d')  # 겹치는 부분이 없는 경우
    elif (p1 == x2 and (q1 == y2 or q2 == y1)) or ((p2 == x1 and (q1 == y2 or q2 == y1))):
        print('c')  # 겹치는 부분이 점인 경우
    elif (p1 == x2) or (p2 == x1) or (q1 == y2) or (q2 == y1):
        print('b')  # 겹치는 부분이 선분인 경우
    else:
        print('a')  # 겹치는 부분이 직사각형인 경우
