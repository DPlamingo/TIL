import sys
sys.stdin = open('input.txt')

# 전체 테스트 케이스 수
# input 함수는 입력 받은 값을 항상 문자열로 반환
# 전체 tc 수 T 만큼 반복해서 코드 실행
# T는 int가 되어야 한다.
T = int(input())

# T번 만큼 순회하면서 각 tc에 대한 문제 해결
# ctrl + shift + f10 -> 코드 실행
for tc in range(T):
    # 상자들이 담겨있는 칸의 개수
    N = int(input())
    # 각 상자들의 높이가 담겨 있는 값을 받는다.
    # 공백을 기준으로 나눠서 입력받은 문자열들
    # 비교하기 쉽게 int로 바꿔서 list에 담는다.
    boxes = list(map(int, input().split()))
    # print(N, boxes)
    # 최종 결괏값
    result = 0
    # 모든 상황에 대한 낙찻값을 위해 전체 순회
    for i in range(N): # N = 9 | 0~8
        # i 번째 상자가 떨어질 수 있는 최대
        # 방해 받지 않고 떨어지는 최대
        # 전체 길이 - 내 위치 + 1
        max_H = N - (i+1)
        # 내 다음에 오는 상자들 중에
        # 나보다 크거나 같은 값들 찾기
        # 내 다음부터 끝까지
        for j in range(i+1, N):
            # 내 높이보다, j번째 위치가 크거나 같은 값
            if boxes[i] <= boxes[j]:
                max_H -= 1
        # i번째 값이 최대로 떨어질 수 있는 낙차 값이
        # 현재 내가 기록해둔 최종 결괏값보다 크다면,
        if result < max_H:
            result = max_H
    print(f'#{tc+1} {result}')
