# 백준 가운데를 말해요

N = int(input())
nums = [int(input()) for _ in range(N)]

temp = []
result = []
for i in nums:
    temp.append(i) # 말한거 적어놓고
    temp.sort() # 일단 정렬
    mid = len(result) // 2 # 중간값 구해야되기때문에
    result.append(temp[mid]) # 지금까지 말한 수 중에 중간값

print(*result, sep='\n')