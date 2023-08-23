# HW 세번째 풀이

hex_to_bin = {hex(i).replace('0x', '').upper() : f'{i:04b}' for i in range(16)}

T = int(input())
for tc in range(1, 1+T):
    N, N16 = input().split()