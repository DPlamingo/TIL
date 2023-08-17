# 회전
import sys
sys.stdin = open('input5097.txt')

from collections import deque
T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    queue = deque(map(int, input().split()))

    for i in range(M):
        queue.append(queue.popleft())

    print(f'#{tc} {queue[0]}')

