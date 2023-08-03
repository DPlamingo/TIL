# start : 시작 지점
# end : 끝 지점
# print(binary_

# binary_search(이진 탐색)

# arr : 원본 배열
# N : 배열의 길이
# key : 타겟

def binary_search(arr, N, key, start, end):
    # start = 0
    # end = N - 1  # 끝 인덱스
    if start > end:  # 시작지점이 끝지점보다 작거나 같은 동안
        return False

    else:
        mid = (start + end) // 2 # 중앙 인덱스

        if arr[mid] == key :
            return True

        if arr[mid] > key :
            return binary_search(arr, N, key, start, end)

        else:
            start = mid + 1
            return binary_search(arr, N, key, start, end)
    # mid = N // 2 # 중앙 인덱스


numbers = list(range(1, 30, 2))
print(numbers)
N = len(numbers)
target = 25

print(binary_search(numbers, N, target, 0, N-1))