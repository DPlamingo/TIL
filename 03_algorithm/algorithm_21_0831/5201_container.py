# 컨테이너 운반

# N 개의 컨테이너, M대의 트럭
# 트럭당 한 컨테이너, 적재용량 초과하면 운반안됨

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    wi = list(map(int, input().split())) # 컨테이너 마다의 무게
    ti = list(map(int, input().split())) # 트럭 용량

    wi.sort(reverse=True)
    ti.sort(reverse=True)
    # print(ti)
    cnt = 0
    for i in range(M):  # 무조건 트럭 갯수 순
        for j in range(len(wi)): # 컨테이너 확인
            if wi == False:
                break

            if ti[i] >= wi[j]:
                cnt += wi.pop(j)
                break # j번째 부숨

    print(f'#{tc} {cnt}')
