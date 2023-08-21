# Tree

# 전위 순회
def preorder(node):
    if node != 0:
        print(node, end=' ')
        preorder(left[node])
        preorder(right[node])


# 중위 순회
def inorder(node):
    if node != 0:
        inorder(left[node])
        print(node, end=' ')
        inorder(right[node])

V = int(input())
E = V - 1
edge = list(map(int, input().split()))

left = [0] * (V+1)
right = [0] * (V+1)
parent = [0] * (V+1)

tree = [[0] * 3 for _ in range(V+1)]
print(tree)

for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    parent[c] = p

    if tree[p][0] == 0:
        tree[p][0] = c

    else:
        tree[p][1] = c
    tree[c][2] = p

print(tree)