def selection_sort(arr):
    for i in range(len(arr)):
        # 뒤에 조사 하는 대상이 클지 작을지 모르므로, 내 위치가 제일 작다고 가정
        min_idx = i  # 0과 1을 표현한거임. 0 > 1 > 2 마음대로 꺼내 쓸려고
        for j in range(i + 1, len(arr)):
            # 현재까지 최소값이 담겨 있다고 판단되는 위치의 값과
            # 새롭게 조사하는 j번째 위치의 값을 크기 비교
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [3, 19, 61, 18, 4, 7, 44, 100]
N = len(arr)
selection_sort(arr)
print(arr)