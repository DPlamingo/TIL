# 빙고 재도전

paper = [list(map(int, input().split())) for _ in range(5)]
signal = [list(map(int, input().split())) for _ in range(5)]

delta = [[0,0],[-1,0],[-1,1],[0,1],[1,1]] # 본인부터 12시에서 시계방향으로 돔

anchor = []
for y in range(5):
    for x in range(5):
        anchor.append(signal[y][x])
# print(anchor)
cnt2 = 0
cnt3 = 0
for i in anchor: # 사회자가 번호를 부름
    cnt2 += 1 # 호출용
    for y in range(5): # 번호를 찾음
        for x in range(5): # 번호를 찾아나섬
            if i == paper[y][x]: # 종이에 번호가 있다?
                paper[y][x] = 0  # 해당 칸을 0으로 만듬

                for dy, dx in delta: # y축 델타, x축 델타 ; 해당칸에서 상하좌우 대각선 확인
                    cnt = 0   
                    for j in range(-5,5):    # 줄 전체 확인용 
                        if cnt == 5:
                            cnt3 += 1
                        else:
                            if 0 <= y+dy*j < 5 and 0 <= x+dx*j < 5: # 상하좌우 대각 범위안이어야함
                                if paper[y+dy*j][x+dx*j] == 0:
                                    cnt += 1
                            
    if cnt3 >= 3:        
        print(cnt2)
        break
                            