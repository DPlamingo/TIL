word = input()

stack = []
cnt = 10
for i in word:
    if stack and stack[-1] == i:
        cnt += 5
    elif stack and stack[-1] != i:
        cnt += 10
    stack.append(i)

print(cnt)