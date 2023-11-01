# 주식 백준 실버2

# 날 별로 비교 그리디하게 푸려면
# 배열을 해서 제일 큰값에 하위 항목을 다 파는게 가장
# 돈 많이 버는 방법임
# 배열 순서로 순회하다가 다음값이 이전 값보다 작으면
# 판단해서 가장 큰 값인지 확인 
# 그리고 남은 값 중에서 큰지 비교
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    stock_price = list(map(int, sys.stdin.readline().split()))

    stock_price.reverse()
    result = 0

    max_value = stock_price[0]

    for i in stock_price:
        if i > max_value:
            max_value = i
        else:
            result += max_value - i
    
    print(result)