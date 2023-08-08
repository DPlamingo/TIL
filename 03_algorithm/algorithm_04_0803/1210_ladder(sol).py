import sys
sys.stdin = open('input1210.txt')

# 필요인자 : 시작 좌표 (x, y)

dx = [1, 0, 0]
dy = [0, -1, 1]

def search(x, y):
    # 각 시작 좌표들 마다 방문 표시를 위한 2차원 리스트 만들기
    visited = [[0]*100 for _ in range(100)]
    # 만약 2를 찾았을 때, 반환해야 할 시작 좌표 y를 기록
    original_y = y
    
    visited[x][y] = 0
    # 조사 조건은 x가 99가 되기 전까지
    while x != 99:
        # 계속 아래로 조사하면서 진행
        # 조사 순서는? 하, 좌 우 ? 하, 우 좌?
        for k in range(3):
            # 다음 조사 위치 좌표
            # 다음 지역 x,y 좌표 | 현재 위치 x,y 좌표 + 다음 방향에 대한 좌표
            nx = x + dx[k]
            ny = y + dy[k]
            
            # 다음 조사를 할 예정인 (nx, ny) 위치가 안전하게 조사 가능한지
            # 조건으로 확인
            # 다음 조사 가능 여부 조건에 data[nx][ny] == 1로 잡을때 발생하는 문제
            if 0 <= nx < 100 and 0 <= ny < 100 and data[nx][ny] and visited[nx][ny] == 0:
                x, y = nx, ny
                # 이전 위치를 0으로 바꾸면 어떨까?
                # data[x][y] = 0
                visited[nx][ny] = 1



    # x가 99가 되는 순간
    if data[x][y] == 2:
        return original_y
    else:
        return '실패'
            
    # 하나, 아래로 조사를 진행 해 나갈 것
    # 둘, 단, 좌, 우 중 갈 수 있는 곳 마주하면, 그쪽으로 먼저 갈것.
    # 셋, 이미 지나온 길은 다시 돌아가지 않도록 해야 함.
    # 넷, 마지막 행(99, n)이 되었을때에는 종료 되어야함
    # 다섯, 마지막 행에서 마주한 값이 2일 경우, 출발 좌표를 출력해야함
    # 여섯, 위 모든 과정을 모든 출발점에 대해서 실행해야함.


# 테스트 케이스 10개
# tc 임시 변수는 최후 출력값에서 tc번호를 표기할 때, 써야해서 1~10

for _ in range(10):
    tc = int(input())
    # 100 * 100 의 2차원 리스트
    # data = []
    # for i in range(100):
    #     arr = list(map(int, input().split()))
    #     data.append(arr)
    data = [list(map(int, input().split())) for _ in range(100)]

    # 모든 출발점 찾기
    for i in range(100):
        # 항상 0번째 열에서 출발
        # 0번째 열의 i번째 행의 값이 1이면
        if data[0][i] == 1:

            result = search(0, i) # 코드 실행 결과 반환 저장
        if result != '실패': # 조사를 한번 끝냈는데, result에 실패 말고 다른게 있다?
            # 값을 찾았으니 종료
            break
            # print(i) # 모든 출발점

    # print(data)
    print(f'#{tc} {result}')