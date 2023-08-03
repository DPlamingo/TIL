import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # print(arr)


# min_m_value = 0
    arrange_list = [] # 빈 리스트 작성
# max_m_value = 0
    for i in range(N-M+1): # 총 배열 갯수 중에서 묶음 값 이전 까지
        arrange_value = 0 # value값 리셋
        for j in range(i, i+M): # 묶음에 대한 for문
            arrange_value = arrange_value + arr[j] # 리스트에 묶음에 대한 값에 대한 합 추가
        arrange_list.append(arrange_value) # 포문 끝나고, 리스트에 추가
        # print(max_M)


    result = max(arrange_list) - min(arrange_list) # 묶음 합 리스트 중에서 max값과 min값의 차이

    print(f'#{tc} {result}')