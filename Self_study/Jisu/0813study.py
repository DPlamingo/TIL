import sys
sys.stdin = open('input0813.txt')

T = int(input())
for tc in range(1, T+1):
    arr = input()
    # print(arr)

    stack = []
    for i in arr:
        # print(i)
        if i == '(' or i == '{' : # arr에 괄호를 만나야함
            stack.append(i) 
            # print(stack)
        if i == ')' :
            if stack and stack.pop() == '(': 
                pass
        
            else:
                stack.append(i)
                           
        if i == '}' :
            if stack and stack.pop() == '{':
                pass
            else:    
                stack.append(i)

    if stack:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')