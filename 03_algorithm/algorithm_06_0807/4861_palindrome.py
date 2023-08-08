import sys
sys.stdin = open('input4861.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]

    def reverse(arg):
        reverse_arg = ''
        for i in arg:
            reverse_arg = i + reverse_arg
            return reverse_arg

    list_args = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            for k in range(N):
                for l in range(M):
                    list_args.append(arr[k][l])
                    args = ' '.join(list_args)
                print(args)
                print('===')
                if args == reverse(args):
                    print(args)


    for j in range(N-M+1):
        for i in range(N-M+1):
            for l in range(N):
                for k in range(M):
                    args = ' '.join(arr[k][l])
                if args == reverse(args):
                    print(args)