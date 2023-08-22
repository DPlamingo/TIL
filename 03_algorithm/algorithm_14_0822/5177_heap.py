import sys
sys.stdin = open('input5177.txt')

def inorder(node):
    global count
    if node <= N:
        # 왼쪽 자식
        inorder(node*2)
        tree[node] = count
        count += 1
        inorder(node*2 + 1)

T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    trees = map(int, input().split())
    # root를 1로 한다
    # tree를 그릴때, 0번은 쓰지 않는다
    # N 노드의 개수
    # tree N + 1만큼 담을 수 있어야한다
    tree = [0] * (N+1)
    count = 1
    inorder(1)
    print(tree)
    print(f'#{tc} {tree[1]} {tree[N//2]}')