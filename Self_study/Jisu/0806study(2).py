# 카운팅 정렬

# 카운팅 정렬 그림부터 생각을 해라
# 1. 카운트가 필요한 리스트 생각
# 2. 리스트 값에 대한 인덱스 갯수에 대한 새 리스트
# 3. 그 리스트 누적
# 4. 누적된 리스트와 기존 데이터 리스트 비교하여 정렬

list_origin = [0,6,3,1,5,5,4,2,2]

list_count_1 = [0] * (max(list_origin) + 1)
list_count_2 = [0] * (len(list_origin))


for i in range(len(list_origin)):
    list_count_1[list_origin[i]] += 1
print(list_count_1)

for i in range(1, len(list_count_1)):
    list_count_1[i] += list_count_1[i-1]

print(list_count_1)

for i in range(len(list_origin)-1, -1, -1):
    print(i)
    list_count_1[list_origin[i]] -= 1
    print(list_count_1)
    list_count_2[list_count_1[list_origin[i]]] = list_origin[i]
    print(list_count_2)

print(list_count_2)