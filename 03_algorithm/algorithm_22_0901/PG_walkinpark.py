# 공원 산책

park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]

way = []
for i in routes:
    way.append(i.split())
print(way)

check = []
cnt = -1
for i in park:
    cnt += 1
    if 'S' in i:
        check = [cnt, i.index('S')]

y = check[0]
x = check[1]
print(y, x,'y','x')
for op, n in way:
    for j in range(int(n)):
        if 0 <= x < len(park[0]) and 0 <= y < len(park):
            if park[y][x] == 'X':
                if op == 'E':
                    x -= 1
                elif op == 'S':
                    y -= 1
                elif op == 'W':
                    x += 1
                elif op == 'N':
                    y += 1
                break
            if op == 'E':
                x += 1
            elif op == 'S':
                y += 1
            elif op == 'W':
                x -= 1
            elif op == 'N':
                y -= 1
        else:
            if op == 'E':
                x -= 1
            elif op == 'S':
                y -= 1
            elif op == 'W':
                x += 1
            elif op == 'N':
                y += 1
print([y,x])


    # for j in range(int(n)):
    #     if op == 'E':
    #         x += 1
    #         routes[]



