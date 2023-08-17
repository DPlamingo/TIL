# 체크할 배열
# 시작점 (현재 조사 위치)
# 종료지점 (모든 원소의 개수가 종료시점 == N)
# 총합 : 누적값 acc
def solution(arr, end, result):
    if result != 10:
        return
    for i in range(1, end+1):
        if arr[i]:
            print(data[i], end =' ')

def construct_candidates(c):
    c[0] = True
    c[1] = False
    return c

def backtracking(arr, now, end, result):
    global count
    if result > 10:
        return

    count += 1
    # 후보군 목록
    # 부분집합의 원소로 now 번째의 값을 사용한다/안쓴다.
    c = [0] * 2

    # 언제까지 조사를 할 것이냐.
    if now == end:
        solution(arr, end, result) # 값을 도출하는 함수를 호출
    else:
        # 아직 조사해야하는 원소가 남았다.
        # 다음 원소를 조사하러 가기 위해 index 1 증가
        now += 1
        # now가 1 증가 된 다음
        # 내가 arr[now] 값을 쓸지 말지를 판별할 수 있는 후보군 만들기
        # arr, 지금까지 사용한 원소 인덱스, 최대 원소 개수, 후보군 목록
        ncandidates = construct_candidates(c)
        # 후보군 수 만큼 반복해서 조사
        for i in range(len(ncandidates)):
            arr[now] = c[i]
            if arr[now]: # 현재 조사하고 있는 대상 쓰기로 했으면,
                # now 번째 원소 쓰기로 했으면,
                # 부분집합의
                backtracking(arr, now, end, result + data[now])
            else:
                # now번째 요소를 안쓴날
                backtracking(arr, now, end, result)


# 유망성 : 다음 조사를 하는 의미가 있는가?
# 후보군 수 : 우리의 후보군이란, 0 1
# MAXCANDIDATES = 2
# 최대 원소 개수
NMAX = 12
count = 0

data = list(range(11))
arr = [0] * NMAX # 각 원소를 사용할 것인가 말것인가 체크
# [1, 2, 3, 4]
# [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
backtracking(arr, 0, 10, 0)
print(count)