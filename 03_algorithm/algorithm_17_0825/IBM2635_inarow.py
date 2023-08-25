# IM 용 줄이어가기

N = int(input())

def check(i):
    regulation = [N]
    regulation.append(i)
    while regulation[-1] >= 0:
        new = regulation[-2] - regulation[-1]
        regulation.append(new)

    regulation.pop()
    return len(regulation), regulation

result = []
for i in range(N,0,-1):
    result.append(check(i))
# print(result)
result2 = []
for i in range(0,len(result)):
    result2.append(result[i][0])
print(max(result2))
for i in result[result2.index(max(result2))][1]:
    print(i, end=' ')
print()