import sys
sys.stdin = open('input0823.txt')

T = int(input())
for tc in range(1, 1+T):
    N, K = map(int, input().split())
    arr = [(input().split()) for _ in range(N)]
    
    arr_symetry = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_symetry[i][j] = arr[j][i]

    list_arr1 = []
    for i in arr_symetry:
        list_arr1.append(''.join(i))

    # print(list_arr1)
    list_arr2 = []
    for i in arr:    
        list_arr2.append(''.join(i))
    # print(list_arr2)


    cnt = 0
    check = '0'
    check2 = ''
    for i in range(K):
        check += '1'
        check2 += '1'
    check = check + '0'
    check3 = '0' + check2
    check2 = check2 + '0'

    # print(check,'111',check2,'222',check3)

    for i in list_arr1:
        cnt += i.count(check)

    for i in list_arr2:
        cnt += i.count(check)


    
    for i in range(N):
        check5 = ''
        check6 = ''
        check7 = ''
        check8 = ''
        for j in range(K+1):
            check5 += list_arr1[i][j]
            check6 += list_arr1[i][-1-j]
            check7 += list_arr2[i][j]
            check8 += list_arr2[i][-1-j]
        if check5 == check2 or check6 == check3 or check7 == check2 or check8 == check3:
            cnt += 1
            print(check5,check6,check7,check8)
    print(f'#{tc} {cnt}')
    
