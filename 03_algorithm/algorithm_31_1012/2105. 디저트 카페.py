# 디저트 카페

# 걍 무적권 우측 아래로 고고
# (1) 전체 배열 순회( 시작점 : si, sj), 사각형
# 되돌아오는 경우 ( 중복x, v[] -> len)
# 선택 해야됨 직진 or 회전
# n : 꺾는 횟수(방향)
# 정답처리 : n==3 & 시작지점 복귀

di = [1, 1, -1, -1, 1]
dj = [-1, 1, 1, -1, -1]

def dfs(n, ci, cj, v):
    global ans
    # 가지치기: 절반을 돌았는데 *2 해도 정답 갱신 불가능
    if n==2 and ans >= len(v) *2:
        return

    if n > 3: # 종료 조건, 계속 도는것 방지
        return

    if n == 3 and (si, sj) == (ci, cj): # 정답처리 조건 ( 시작지점 복귀)
        ans = max(ans, len(v)) # 와서 더 와봣자 체크해야됨..
        return

    for k in range(n, n+2): # n방향 n+1 방향
        ni, nj = ci+di[k], cj+dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in v:
            v.append(arr[ni][nj])
            dfs(k, ni, nj, v)
            v.pop()


# 비밀 A형 레시피
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1

    for si in range(N-2):
        for sj in range(1, N-1):
            dfs(0, si, sj, [])
    print(f'#{tc} {ans}')