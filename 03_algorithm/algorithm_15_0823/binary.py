# HW

T = int(input())

for tc in range(1, 1+T):
    N, N16 = input().split()
    print(f'#{tc}',end=' ')
    for char in N16:
        print(f'{bin(int(char, base=16))[2:].zfill(4)}',end='')
    print()