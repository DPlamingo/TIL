# 중위순회

import sys
sys.stdin = open('input1231.txt')

tc = 0
while True:
    tc += 1
    try:
        def inorder(node):
            if node <= N:
                inorder(node*2)
                print(trees[node], end='')
                inorder(node*2+1)

        N = int(input())
        trees = [0]*(N+1)
        for i in range(N):
            tree = list(input().split())
            trees[i+1] = tree[1]

        print(f'#{tc}',end=' ')
        inorder(1)
        print()

    except EOFError:
        break