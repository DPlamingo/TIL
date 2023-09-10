import sys
sys.stdin = open('input0826.txt')

def calculate_profit(N, M, city):
    max_profit = 0
    
    for K in range(1, N+1):
        operation_cost = K * K + (K - 1) * (K - 1)
        
        for i in range(N):
            for j in range(N):
                homes_covered = 0
                profit = 0
                
                for x in range(i-K+1, i+K):
                    for y in range(j-K+1, j+K):
                        if 0 <= x < N and 0 <= y < N:
                            if city[x][y] == 1:
                                profit += M
                                homes_covered += 1
                
                if profit - operation_cost >= 0 and homes_covered > max_profit:
                    max_profit = homes_covered
    
    return max_profit

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    result = calculate_profit(N, M, city)
    print(result)  # 최대 서비스 제공 집의 수 출력
