# DP 연습문제 3
import sys
sys.stdin = open('inputex1.txt')

arr = list(map(int, input().split(',')))
print(arr)

def build_graph(input_value):
    graph = {}
    for i in range(0, len(input_value), 2):
        key, value = input_value[i], input_value[i+1]
        if key not in graph:
            graph[key] = []

        if value not in graph:
            graph[value] = []

        graph[key].append(value)
    return graph

def DFS(graph, start_node):
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(sorted(graph[node], reverse = 1))
            # print(stack)

DFS(build_graph(arr), 1)
