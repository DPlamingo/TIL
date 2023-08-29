# N개의 물건
# 각 물건의 무게 W
# 가치 V
# 가치의 최대값은?
# 배낭의 총 무게제한 K
N, K = map(int, input().split())  # 물품수, 버틸수있는 무게
# 걍 무게 합 되기 전 최대값
arr = [list(map(int, input().split())) for _ in range(N)]
W = []
V = []
for w,v in arr:
    W.append(w) # 무게만 든 리스트
    V.append(v) # 가치만 든 리스트

result = [] # 만족하는 최대 가치를 넣기위한 리스트
for i in range(N): # 순서대로 집어넣고, 그 다음애들이 들어갈 수 있는지 비교를 위한 초석
    cnt = V[i] # 가치
    weight = W[i] # 무게
    if i+1 < N: # 지금 순서가 마지막이라면, 지금가치가 최대값임
        for j in range(N): # 착착착착 다음꺼 넣을 수있는지
            if i == j:
                rest = K - weight # 무게에서 뺀값
            if rest >= W[j]: # 남은 무게에 들어감?
                weight += W[j] # 무게 증가시키고
                cnt += V[j] # 가치를 넣는다
    result.append(cnt) # 가치 보관

print(max(result)) # 최대 가치 출력