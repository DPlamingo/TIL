# 미로의 거리
import sys
sys.stdin = open('input5105.txt')


# 0의 거리를 건너 출발 값 2에서 도착 지점 3을 찾는다.
# 길이 있으면, 최소 칸수(BFS) 을 출력한다.
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 자 일단 2의 위치를 찾는다.
    go = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                go.append([i,j])

    # i,j 가 2의 위치이다.
    # y,x 꺼냄
    # y = go[0][0]
    # x = go[0][1]
    # 중복값을 제거해줄 녀석 등장
    visited = []
    # 이다음으로, i,j의 델타탐색으로 길을 찾는다.
    # 델타탐색을 만들고,
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    # 델타탐색이 범위 내에서 가동
    # y2 = y
    # x2 = x
    # print(y2, x2)
    visitedcnt = []
    # cnt = 0
    def BFS(arr):
        while go: # 정지시키면 그만한다.
            gopop = go.pop(0) # 큐에 있는애 제거
            visited.append(gopop) # 중복되나 확인
            # visitedcnt.append()
            # cnt += 1
            for i in range(4): # 델타 순회
                y2 = gopop[0] + di[i]
                x2 = gopop[1] + dj[i]

                if 0 <= y2 < N and 0 <= x2 < N:
                # 범위가 벗어나지 않는다면
                    if arr[y2][x2] == 0 and [y2,x2] not in visited:
                        # 주변에 0이 있다면, 그 인덱스를 go에 추가
                        go.append([y2,x2])
                        # cnt += 1
                        # if cnt = 1:
                        #     cnt1 += 1
                        # 그럼 다시 가야지? 언제까지? 3될때까지
                    # print(go)
                    if arr[y2][x2] == 3:
                        # print(cnt)
                        break
        return 0

    print(BFS(arr))
