import sys
sys.stdin = open('input1.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

