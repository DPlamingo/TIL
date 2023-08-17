# 선형 Queue (느림)

# queue = []
# queue.append('A')
# queue.append('B')
# print(queue)
# print(queue.pop(0))
# print(queue)

from collections import deque # double ended queue 약자임
queue = deque()
queue.append('A')
queue.append('B')
print(queue)
print(queue.popleft()) # 팝하면 top이 빠지니 왼쪽 팝하면 0 뺌.
