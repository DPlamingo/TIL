# 인접리스트
# 갈 수 있는 지점만 저장하자
# 주의사항
# - 각 노드마다 갈 수 있는 지점의 개수가 다름
# -> range 할 때 index 조심
# 메모리가 인접 행렬에 비해 훨씬 효율적이다.
graph = [
    [1,3],
    [0,2,3,4],
    [1],
    [0,1,4],
    [1,3],
]


# DFS
# stack 버전
def dfs_stack(start):
    visited = []
    stack = [start]

    while stack:
        now = stack.pop()
        # 이미 방문한 지점이라면 continue
        if now in visited:
            continue

        # 방문하지 않은 지점이라면, 방문표시
        visited.append(now)

        # 갈 수 있는 곳들을 stack 에 추가
        for to in range(len(graph[now])-1, -1, -1):
            # 연결이 안되어 있다는건 애초에 저장하지 않았으므로
            # 체크할 필요가 없음
            # if graph[now][next] == 0:
            #     continue
            next = graph[now][to]
            # 방문한 지점이라면 stack에 추가하지 않음
            if next in visited:
                continue

            stack.append(next)
    # 출력을 위한 반환
    return visited


print('dfs stack = ', end='')
print(*dfs_stack(0))

# DFS - 재귀
# Map 크기(길이)를 알때, append 형식 말고 아래와 같이 사용하면 훨씬 빠르다.
visited = [0] * 5
path = []  # 방문 순서 기록


def dfs(now):
    visited[now] = 1  # 현재 지점 방문 표시

    path.append(now)
    # 인접한 노드들을 방문
    for to in range(len(graph[now])):
        # if graph[now][next] == 0:
        #     continue
        next = graph[now][to]
        if visited[next]:
            continue

        dfs(next)
print('dfs 재귀 =', end=' ')
dfs(0)
print(*path)

    # 기저 조건

    # 들어가기 전
    # 함수 호출
    # 돌아와서

# 인접리스트