# HW

import sys
sys.stdin = open('input1240.txt')

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())

    arr = [input() for _ in range(N)]
    # print(arr)

    list_arr = []
    for i in arr:
        if '1' in i:
            list_arr.append(i)
    # print(list_arr)

    # print(reversed(list_arr[0]),'sort')

    sort = ''.join(reversed(list_arr[0]))
    # print(sort)
    cnt = 0
    for i in sort:
        cnt += 1
        if i == '1':
            break

    #
    # for i in range(len(list_arr)):
    #     for j in list_arr:
    #         left = len(j) % 7
    #         for k in range(left):
    #             list_arr[i].pop()
    #
    # list_arr = ''.join(list_arr)

    nums = {
        '0001101' : '0' ,
        '0011001' : '1' ,
        '0010011' : '2' ,
        '0111101' : '3' ,
        '0100011' : '4' ,
        '0110001' : '5' ,
        '0101111' : '6' ,
        '0111011' : '7' ,
        '0110111' : '8' ,
        '0001011' : '9' ,
    }
    # print(cnt, 'cnt')
    binary = []
    for i in range(len(list_arr[0])-cnt-55,len(list_arr[0])-cnt+1,7):
        binary_cal = ''
        # print(i,'i')
        for j in range(i,i+7):
            binary_cal += list_arr[0][j]
        binary.append(binary_cal)
    # print(binary)

    code = ''
    for i in binary:
        # print(i,'i')
        if i in nums:
            code += nums[i]
    # print(code)

    code2 = 0
    for i in range(0,len(code),2):
        # print(i, '디버깅 i')
        code2 += int(code[i])
    # print(code2, '2임')

    code3 = 0
    for i in range(1,len(code),2):
        code3 += int(code[i])

    check = (code2*3 + code3)

    result = 0
    if check % 10 == 0:
        for i in code:
            result += int(i)
        print(f'#{tc} {result}')


    else:
        print(f'#{tc} 0')