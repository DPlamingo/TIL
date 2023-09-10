# calculation2

while True:
    T_len = int(input())
    value = input()

    stack = []
    stack_sub = ''
    for i in value:
        if i == stack_sub:
            stack_sub += i
        if i in '+*':
            if i == '+' and stack == False :
                stack.append(i)
            elif i == '+' and (stack[-1] == '+' or stack[-1] == '*'):
                stack_sub += i
            elif i == '*' and (stack[-1] == '+' or stack == False):
                stack.append(i) 
            elif i == '*' and stack_sub[-1] == '*':
                stack_sub += i
        for j in range(len(stack)):
            stack_sub += stack.pop()