n = str.upper(input())
print(n)
list_count = []
cnt = 0
for i in range(len(n)):
    for j in range(i, len(n)):
        if n.count(n[i]) == n.count(n[j]):
            cnt += 1
            list_count.append(n.count(n[i]))
if cnt > 1:
    print('??')
else:
    print(list_count[i])
