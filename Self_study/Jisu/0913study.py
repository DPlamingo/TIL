# 백준 실4

N, M = map(int, input().split())
packages = [list(map(int, input().split())) for _ in range(M)]

sets = []
each = []
for y,x in packages:
    sets.append(y)
    each.append(x)

sets_min = min(sets)
each_min = min(each)

check = []
if N >= 6:
    value = N // 6
    rest = N % 6
    check.append((value+1)*sets_min)
    check.append(N*each_min)
    check.append(value*sets_min+rest*each_min)
    print(min(check))    
else:
    check.append(N*each_min)
    check.append(sets_min)
    print(min(check))