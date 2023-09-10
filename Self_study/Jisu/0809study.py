import sys
sys.stdin = open('input0809study.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())


    list_storage = []
    for i in range(1, N+1):
        list_storage.append(i)
    for i in range(N, 0, -1):
        list_storage.append(i)
    # print(list_storage)

    list_tri_pascal = []
    for i in range(1<<len(list_storage)):
        list_pascal = []

        for j in range(len(list_storage)):
            if i & (1<<j):
                list_pascal.append(list_storage[j])
                # print(list_pascal)
        list_tri_pascal.append(list_pascal)
               
    for k in range(1,N+1):
        for row in list_tri_pascal:
            if sum(row) == 2**k and row == row.reverse():
                print(row)