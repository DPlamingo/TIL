# 백준 브2 팰린드룸

word = input()

result = ''
for i in word:
    result = i + result

if result == word:
    print(1)
else:
    print(0)