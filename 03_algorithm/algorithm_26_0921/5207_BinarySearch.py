# 이진 탐색

# 일단 정리해보자
# 리스트 개수 N개인 리스트 A
# 리스트 개수 M개인 리스트 B
# 탐색구간 시작을 l, 끝을 r 이라하면
# 중심은 m = (l+r)//2 이고,
# 왼쪽 구간은 l에서 m-1, 오른쪽은 m+1부터 r까지
# 근데 번갈아 가면서, 찾아야됨.

def BinarySearch(l,r,target):
    global cnt
    for _ in range(N+1): # 타겟을 발견 할때까지 반복
        m = (l+r)//2 # 중간 인덱스
        # print('#', cnt, target)
        # print(m)
        if target == A[m]: # 중간 인덱스가 타겟이면 끝
            return 1

        elif target > A[m]: # 타겟이 중간값보다 크다면, 근데 번갈아 가면서 가야되기때문에
            if cnt == 1:
                return 0
            else:
                # 조건을 cnt 짝수로 줘버림
                cnt = 1
                l = m+1 # 위치를 바꿔줌

        elif target < A[m]:
            if cnt == 0:
                return 0
            else:
                # 조건을 cnt 홀수로 줘버림
                cnt = 0
                r = m-1

    return 0


T = int(input())
for tc in range(1, 1+T):
    N, M = map(int,input().split())
    A = list(map(int,input().split())) # N개에 대한 리스트
    B = list(map(int,input().split())) # M개에 대한 리스트
    A.sort()


    result = 0
    for i in B:
        cnt = 2
        result += BinarySearch(0,N-1,i)
    print(f'#{tc} {result}')