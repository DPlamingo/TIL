# 그래프 경로 stack.1
import sys
sys.stdin = open('input4871.txt')

T = int(input())
for tc in range(1, 1+T):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    # print(S, G)
    # print(f'시작임')
    def dic_arr(list_arr):
        graph = {}
        for i in range(len(list_arr)):
            key, value = list_arr[i][0], list_arr[i][1]
            # print(key, value)
            if key not in graph:
                graph[key] = []
            if value not in graph:
                graph[value] = []
            graph[key].append(value)
        # print(graph)
        return graph

    # print(dic_arr(arr))

    def path(graph, start, end):
        visited = set()
        stack = [start]
        list_node = []
        while stack:
            node = stack.pop()
            list_node.append(node)
            if node == end:
                return True
            if node not in visited:
                visited.add(node)
                stack.extend(sorted(graph[node], reverse = True))

        return False
            # print(list_node)

    graph = dic_arr(arr)
    result = path(graph, S, G)
    print(f'#{tc} {result}')





    # print(arr)