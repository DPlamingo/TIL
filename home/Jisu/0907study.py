# 백준 섬의 개수
import sys
sys.stdin = open('input0907.txt')


while True:
    try:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        land = [list(map(int, input().split())) for _ in range(h)]

        delta = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

        cnt = 0
        for i in range(h):
            for j in range(w):
                if land[i][j] == 1:
                    cnt += 1
                    y, x = i, j
                    land[y][x] = 0
                    while True:
                        for dy, dx in delta:
                            ny, nx = y + dy, x + dx
                            if 0 <= ny < h and 0 <= nx < w:
                                if land[ny][nx] == 1:
                                    land[ny][nx] = 0
                                    y, x = ny, nx
                                    break
                        else:
                            break  # 이중 루프 탈출

        print(cnt)
    except:
        break