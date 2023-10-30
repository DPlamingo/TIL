# 백준 실버4 게임을 만든 동준이 2847

# N개의 테케인데 다음 항목보다 무조건 1작아야함
# 뒤에서 부터 다음 인덱스랑 계속 비교하면서 내리고 cnt 를셈
N = int(input())
score = [int(input()) for _ in range(N)]
scores = [0]*N
for i in range(N):
    scores[N-i-1] = score[i]

cnt = 0
for i in range(len(scores)-1):
    # print(scores)
    if scores[i+1] >= scores[i]:
        cnt += scores[i+1] - scores[i] + 1 
        scores[i+1] = scores[i] - 1 

print(cnt)

