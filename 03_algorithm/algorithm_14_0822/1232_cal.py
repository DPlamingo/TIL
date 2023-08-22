# 중위 순회 사칙 연산

import sys
sys.stdin = open('input1232.txt')


tc = 0

def inorder(node):
    if node <= N:
        node_left = inorder(node * 2)
        current_value = trees[node]
        node_right = inorder(node * 2 + 1)

        if current_value == '+':
            return int(node_left) + int(node_right)
        elif current_value == '-':
            return int(node_left)- int(node_right)
        elif current_value == '*':
            return int(node_left)* int(node_right)
        elif current_value == '/':
            if node_right != 0:
                return int(node_left)// int(node_right)
            else:
                return 0
        else:
            return current_value

while True:
    tc += 1
    try:
        N = int(input())
        trees = [0] * (N + 1)
        for i in range(N):
            tree = list(input().split())
            trees[i+1] = tree[1]
        result = inorder(1)
        print(f'#{tc} {result}')

    except EOFError:
        break