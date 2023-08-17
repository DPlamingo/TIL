''''''
#342*15-/+
''''''

fx = '342*15-/+'
stack = [0]*100
for x in fx:
    if x.isnumeric():
        stack.append(x)
    elif x in '*+-/':
        a = int(stack.pop())
        b = int(stack.pop())
        if x == '*':
            c = b* a
        elif x == '+':
            c = b+a
        elif x == '-':
            c = b-a
        elif x == '/':
            c = b/a
        stack.append(c)

d = stack[-1]
print(d)

    #
    #     c = int(b) cal int(a)
    #     stack.append(c)
    #
    # elif stack == 1 and stack[-1] == int:
    #     d = stack.pop()
    #
    # print('d')

# type(/)