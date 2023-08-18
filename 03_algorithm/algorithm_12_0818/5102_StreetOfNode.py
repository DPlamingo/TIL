# 노드의 거리
import sys
sys.stdin = open('input5102.txt')


T = int(input())
for tc in range(1, 1+T):
    V, E = map(int, input().split())
    list_nodes = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    # print(list_nodes)

    def make_dic(arrs):
        graph = {}
        for i in range(0, E):
            node1, node2 = arrs[i][0], arrs[i][1]
            if node1 not in graph:
                graph[node1] = []
            if node2 not in graph:
                graph[node2] = []
            graph[node1].append(node2)
            graph[node2].append(node1)
        return graph

    # print(make_dic(list_nodes))
    cnt = 0
    def bfs(graph, start, end):
        visited = []
        queue = [(start,0)]

        while queue:  # 스택 돌리고
            node, distance = queue.pop(0)  # 큐 없에고
            # list_node.append(node)
            if node == end:  # 도착했나?
                return distance
            if node not in visited:  # 왔던 곳이냐?
                visited.append(node)  # 안왔으면, 들렸다고 적어놓고
                for i in graph[node]:
                    queue.append((i, distance + 1))
        return 0

    print(f'#{tc} {bfs(make_dic(list_nodes),S,G)}')