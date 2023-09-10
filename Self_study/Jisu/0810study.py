# IM 대비 방배정

import sys
sys.stdin = open('input0810study.txt')

T, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(T)]

# print(arr.count(list_cnt))
list_cnt = []
cnt1 = 0 # 초과 방 개수 세기
# cnt2 = 0

k = 0 # 넘기기용
for i in arr:
    if i in list_cnt:
        continue
    else:
        list_cnt.append(i)

for i in arr:
    if arr.count(i) > K:
        cnt1 += 1


result = len(list_cnt) + cnt1//K

print(result)


# 
