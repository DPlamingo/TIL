import sys
sys.stdin = open('input4873.txt')


T = int(input())
for tc in range(1, 1+T):
    N = input()

    def what_is_stack(arg):

        list_stack = [0]

        for char in arg:
            if list_stack[-1] == char:
                list_stack.pop()
            else:
                list_stack.append(char)
        return len(list_stack)-1

    print(f'#{tc} {what_is_stack(N)}')
