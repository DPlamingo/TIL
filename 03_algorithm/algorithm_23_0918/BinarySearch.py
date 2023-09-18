# 이진 탐색(정렬된 상태여야함)

def binarySearch(target):
    global cnt
    low = 0
    high = len(arrN) - 1

    # low > high 라면 데이터를 못 찾는 경우,
    while low <= high:
        mid = (low+high)//2


        # 1. 가운데 값이 정답인 경우,
        if arrN[mid] == target:
            return 1
        # 2. 정답보다 작은 경우,
        elif arrN[mid] < target:
            if cnt == 2 or cnt % 2 == 0:
                cnt = 2*cnt
                low = mid + 1
            else:
                return 0
        # 3. 정답보다 큰 경우,
        else:
            if cnt == 2 or cnt % 2 == 1:
                cnt = 2*cnt - 1
                high = mid - 1
            else:
                return 0
    return 0

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int,input().split())
    arrN = sorted(list(map(int, input().split())))
    arrM = list(map(int, input().split()))
    cnt = 2
    # print(arrM)
    result = 0
    for i in arrM:
        # print(i, binarySearch(i))
        result += binarySearch(i)

    print(f'#{tc} {result}')