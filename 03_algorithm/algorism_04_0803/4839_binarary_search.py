import sys
sys.stdin = open('input4839.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    P = arr[0] # 전체 쪽수
    Pa = arr[1] # A가 찾을 번호
    Pb = arr[2] # B가 찾을 번호
    count_a = 0
    count_b = 0

    def binary_search(pages, key):
            start = 1
            end = pages
            count_num = 0
            list_book = list(range(start, end+1))
            while start <= end :
                mid = int((start + end) / 2)  # 중간 페이지
                if mid == key: # 검색 성공
                    return count_num
                elif mid > key:
                    end = mid - 1

                else :
                    start = mid + 1
                count_num += 1


    count_a = binary_search(P, Pa)
    # print(count_a)
    count_b = binary_search(P, Pb)
    # print(count_b)
    if count_a < count_b:
        print(f'#{tc} A')

    elif count_a > count_b:
        print(f'#{tc} B')

    else:
        print(f'#{tc} 0')