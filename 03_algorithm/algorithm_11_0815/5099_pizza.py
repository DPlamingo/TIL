import sys
sys.stdin = open('input5099.txt')

from collections import deque

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    Ci = deque(map(int, input().split()))
    # Ci = [[idx, val] for idx, val in enumerate(list(map(int, input().split())), 1)]


    queue = deque() # 화덕
    # queue.append(Ci)
    count = deque() # 가상화덕

    # for (idx, val) in enumerate(Ci, 1):
    #     queue.append((idx, val))

    for i in range(N):
        queue.append(Ci[i]) # 초기 값을 주고
        count.append(i+1)
    # print(queue)

    cnt = 0
    while len(queue) != 1: # queue 값이 하나남으면 끝남 무한 순회
        half_count = count.popleft()
        half_Ci = queue.popleft() // 2 # 치즈 반깍기
        if  half_Ci != 0: # 치즈깍기가 0이 아니라면
            queue.append(half_Ci) # 마지막에 추가해줌
            count.append(half_count)
        else: # 0이 됫다면 나가리 시키고 다른친구 들려옴
            cnt += 1
            if cnt <= M - N:
                queue.append(Ci[N+cnt-1]) # 나가면 한단계씩 올라감
                count.append(N+cnt)
    # 우리가 문제에서 필요한건 피자 번호
    # print(Ci.index(count[0]))
    print(f'#{tc} {count[0]}')
