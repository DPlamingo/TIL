# 후위 표기법

susic = '2+3*4/5'
result = ''
result2 = ''
stack = []
stack2 = []
for x in susic:
    if x.isnumeric():
        stack.append(x)
    elif x in '+*/()':
        if x == '(':
            stack2.append(x) # 우선순위 제일 높으므로 push 해줌
        elif x in '*/': # 마지막 값이 나와 같은 */일때까지 뺌
            while stack2 and stack2[-1] in '*/':

            pass
        elif x in '+-':
            pass
        elif x == ')':
            pass

for i in stack:
    result += i

for j in stack2:
    result2 = j + result2

result3 = result + result2
print(result3)