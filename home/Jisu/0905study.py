T = int(input())
for tc in range(1,1+T):
    A, B = map(int, input().split())

    mult = A*B

    cnt = 0
    if A>B:
        for i in range(1,B+1):
            if B % i == 0:
                if A % i ==0:
                    cnt = i
    else:
        for i in range(1,A+1):
            if A % i == 0:
                if B % i ==0:
                    cnt = i
    result = mult//cnt

    print(result)