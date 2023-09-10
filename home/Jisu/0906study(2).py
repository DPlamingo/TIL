#백준 실5 그룹 단어 체커

T = int(input())
cnt = 0
for tc in range(1, 1+T):
    word = input()

    stack = []
    visited = []
    # print(len(word))
    # print(cnt)
    # print(cnt)
    for i in word:
        if i not in visited:
            if stack and stack[-1] != i:
                visited.append(stack[-1])
                stack.append(i)
            else:
                stack.append(i)
        else:
            cnt += 1
            break

print(T - cnt)