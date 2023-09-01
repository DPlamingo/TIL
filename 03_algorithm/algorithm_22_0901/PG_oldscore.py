# 추억의 점수

name = ["kali", "mari", "don"]
yearing = [11, 1, 55]
N = len(name)
photo = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]

result = []
for i in photo:
    cnt = 0
    # print(i)
    for j in range(N):
        # print(j)
        if name[j] in i:
            cnt += yearing[j]
    result.append(cnt)

print(result)