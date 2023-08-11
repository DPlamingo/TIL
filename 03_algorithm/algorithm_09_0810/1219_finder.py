import sys
sys.stdin = open('input1219.txt')


while True:
    try:
        T, K = map(int, input().split())
        arr = list(map(int, input().split()))
        # print(arr)

        def dic_arr(list_arr):
            graph = {}
            for i in range(0, 2*K, 2):
                key, value = list_arr[i], list_arr[i+1]
                if key not in graph:
                    graph[key] = []
                if value not in graph:
                    graph[value] = []
                graph[key].append(value)
            return graph

        # print(dic_arr(arr))

        def DFS(graph, start, end):
            visited = set()
            stack = [start]
            list_node = []

            while stack:
                node = stack.pop()
                list_node.append(node)
                if node == 99:
                    return int(True)

                if node not in visited:
                    visited.add(node)
                    stack.extend(sorted(graph[node], reverse = True))

            return int(False)

        graph = dic_arr(arr)
        result = DFS(graph, 0, 99)
        print(f'#{T} {result}')

    except EOFError:
        break