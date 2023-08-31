N = 10
a = [1, 4, 1, 6, 6, 10, 5, 7, 3, 8, 5, 9, 3, 5, 8, 11, 2, 13, 12, 14]

meet = []
for i in range(N):
    meet.append([a[i*2], a[i*2+1]])
print(meet)
meet.sort(key=lambda x:x[1]) # stable 정렬
meet = [[0,0]] + meet

s = []
j = 0
print(meet)

for i in range(1, 1+N):
    if meet[i][0] >= meet[j][1]: # si >= fj
        s.append(i)
        j = i
print(s)