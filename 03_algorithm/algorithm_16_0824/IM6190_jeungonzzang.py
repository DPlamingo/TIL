# IM 대비용 정곤이읭 단조

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    A = list(map(int, input().split()))

    mult = []
    for i in range(N-1):
        for j in range(i+1,N):
            mult.append(str(A[i]*A[j]))

    print(mult)


    danjo = []
    for i in mult:
        # i = str(i)
        print(i)
        # print(''.join(sorted(i)),'sort')
        list_i = list(i)
        print(list_i,'list i')

        if len(list_i) > 1:
            # print(list_i.sort())
            sort_i = ''.join(list_i.sort())
        else:
            sort_i = i
        if sort_i == i:
            # print(sorted(i),'so')
            danjo.append(int(i))

    print(danjo)
    if danjo:
        print(f'#{tc} {max(danjo)}')
    else:
        print(f'#{tc} -1')
