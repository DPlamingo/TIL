# 1952.수영장

# 1일 10원, 1달 40원, 3달 100원, 1년 300원
# 기본은 1년 시작, 그다음 전체 일수 비교, 그 다음 전체 달 수 비교
# 설계만 하면 답이보임...


def dfs(n, sm):
    global ans
    if n > 12: # 달 수
        ans = min(ans, sm)
        return

    dfs(n+1, sm+day*lst[n]) # 일간권
    dfs(n+1, sm+mon) # 월간권
    dfs(n+3, sm+mon3) # 분기권
    dfs(n+12, sm+year)

T =int(input())
for tc in range(1, 1+T):
    day, mon, mon3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))
    ans = 3000*12

    dfs(1, 0) # n = depth, sm = 합계임

    print(f'#{tc} {ans}')

