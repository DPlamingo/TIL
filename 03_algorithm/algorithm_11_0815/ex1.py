import sys
sys.stdin = open('inputex1.txt')


tc = 0
while True:
    try:
        tc += 1
        T = int(input())
        height = list(map(int, input().split()))

        cnt = 0
        for i in range(2, T-2):
            if height[i] > height[i-1] and height[i] > height[i-2] and height[i] > height[i+1] and height[i] > height[i+2]:
               cnt += height[i] - max(height[i-2],height[i-1],height[i+1],height[i+2])

        print(f'#{tc} {cnt}')

    except EOFError:
        break