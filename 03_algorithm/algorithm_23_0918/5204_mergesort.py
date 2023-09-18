# 병합정렬

def merge_sort(arr):
    # 배열의 길이가 1 이하라면 이미 정렬된 것으로 본다.
    if len(arr) <= 1:
        return arr

    # 배열을 두 부분으로 나눈다.
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # 각 부분을 재귀적으로 정렬한다.
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # 정렬된 두 부분을 병합한다.
    return merge(sorted_left, sorted_right)


def merge(left, right):
    global cnt
    result = []
    left_idx = right_idx = 0

    # print(left, right)
    if left[-1] > right[-1]:
        cnt += 1

    # left와 right의 원소를 비교하면서 result에 넣는다.
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # 남은 원소들을 result에 추가한다.
    while left_idx < len(left):
        result.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        result.append(right[right_idx])
        right_idx += 1

    # if left and right and left[-1] > right[-1]:
    #     cnt += 1
    value = result
    return value

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
# arr = [38, 27, 43, 3, 9, 82, 10]

    sorted_arr = merge_sort(arr)
    print(f'#{tc} {sorted_arr[N//2]} {cnt}')

# 지식의 가치 = 돈으로 매길수 없음, 아르테일 토비한장으로 받음.

# # 예제 사용
# print("Sorted array:", sorted_arr, cnt)






#
# def mergesort(arr,start,end):
#     if start < end:
#         mid = cal(arr, start, end) # 피봇 찾는거
#         mergesort(arr, start, mid)
#         mergesort(arr, mid+1, end)
#
# def cal(arr,start, end):
#     i = start-1
#     j = start
#     pivot = arr[end]
#     while j < end:
#         if pivot > arr[j]: #