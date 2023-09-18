# 퀵 정렬

# 배열
# 왼쪽, 오른쪽 (idx)
def quick_sort(arr, left, right):
    # 분할 정복의 가장 핵심
    # 정복 대상의 범위를 가장 작아질 때 까지 쪼갠다.
    if left < right:
        mid = cal(arr, left, right)
        quick_sort(arr, left, mid-1)
        quick_sort(arr, mid+1, right)

# lounuto => 피봇을 가장 오른쪽 원소로 결정.
def cal(arr, left, right):
    # i = 피봇보다 큰 구간의 왼쪽 경계
    i = left - 1
    # j = 피봇보다 큰 구간의 오른쪽 경계
    j = left
    pivot = arr[right]
    while j < right:
        # 피봇이 j번째 값보다 더 크면,
        if pivot > arr[j]:
            i += 1
            if i < j:
                arr[i],arr[j] = arr[j],arr[i]
        j += 1
    arr[i+1],arr[right] = arr[right],arr[i+1]
    # print(left, right)
    # print(arr)
    return i+1

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))


# nums = [11, 46, 23, 51, 28, 34]
    quick_sort(arr,0,len(arr)-1)
    print(f'#{tc} {arr[N//2]}')
