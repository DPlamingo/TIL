import sys
sys.stdin = open('input1221.txt')

T = int(input())
for tc in range(1, 1+T):
    tcN, N = map(str, input().split())
    list_N = list(map(str, input().split()))
    int_N = int(N)
    # 값을 인덱스로 지정해준다.
    # 인덱스 순서대로 정렬하면 안되나?
    strings = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    for i in range(int_N-1, 0, -1):
        for j in range(i):
            if strings.index(list_N[j]) > strings.index(list_N[j+1]):
                list_N[j], list_N[j+1] = list_N[j+1], list_N[j]


    print(f"{tcN} {' '.join(list_N)}")

