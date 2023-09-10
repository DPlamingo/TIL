N = int(input())  # 참외 개수

yellow_melon = [list(map(int, input().split())) for _ in range(6)]


x = 0
y = 0
list_x = [0]
list_y = [0]

for key, value in yellow_melon:
    if key == 4:
        x += value
        list_x.append(x)
        list_y.append(y)
    if key == 3:
        x -= value
        list_x.append(x)
        list_y.append(y)
    if key == 2:
        y += value
        list_x.append(x)
        list_y.append(y)
    if key == 1:
        y -= value
        list_x.append(x)
        list_y.append(y)
list_x.append(0)
list_y.append(0)


result1 = 0
result2 = 0
for i in range(len(list_x)-1):
    result1 += list_x[i] * list_y[i+1]  
    result2 += list_x[i+1] * list_y[i]

result = abs(result1 - result2)//2
print(result * N)