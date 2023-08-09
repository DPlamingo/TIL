import sys
sys.stdin = open('input4866.txt')


T = int(input())
for tc in range(1, 1+T):
    N = map(str, input())
    # 어떤 인풋값에서 괄호의 순서가 맞는지 확인

    def what_is_stack(arg): # 함수 지정
        list_stack = [] # 빈 스택 하나 만들어 놓고
        for char in arg: # 인풋값을 하나씩, 인자에 할당
            if char == '(' or char == '{': # 그 인자가 괄호 시작 일 경우,
                list_stack.append(char) # 빈 스택에 추가
            elif char == ')': # 그 인자가 괄호 끝일 경우, 두가지로 나눔
                if list_stack.pop() != '(' : # 중괄호끼리 매치가 맞는지 확인, top 제거
                    return False # 아니면, false

            elif char == '}':
                if list_stack.pop() != '{': # 대괄호끼리 매치가 맞는지 확인하고, top 제거
                    return False # 아니면, false

        return len(list_stack) == 0 # 괄호끼리, 매치도 맞다면, top은 -1 즉 빈 스택이됨


    print(f'#{tc} {int(what_is_stack(N))}') # 결과값을 int로 반환하라고 함

