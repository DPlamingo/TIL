def dfs(start):
    stack = [start]
    visited = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.append(node)

    return visited


dfs()