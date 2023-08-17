# 암호 생성기

import sys
sys.stdin = open('inputpassword.txt')

from collections import deque

while True:
    try:
        tc = int(input())
        password = deque(map(int, input().split()))
        # print(tc)
        # print(password)
        cnt = 0
        while password[-1] > 0:
            cnt += 1
            password.append(password.popleft()-cnt)

            if cnt == 5:
                cnt = 0
            # print(cnt)
            # print(password)

        password[-1] = 0

        print_password = ''
        for i in password:
            print_password += ' ' + str(i)
        print(f'#{tc} {print_password}')

    except EOFError:
        break