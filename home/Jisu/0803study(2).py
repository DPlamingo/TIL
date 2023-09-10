import sys
sys.stdin = open('input0803study(2).txt')

T = int(input())
for tc in range(T):
    N = int(input())
    print(N)
    print('=====')


    list_sum = []
    for i in range(N):
        for j in range(N):
            if (i**2) + (j**2) <= N**2:
                list_sum.append([i, j])
                
    result = len(list_sum)*2 + 1 

    print(result)