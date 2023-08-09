import sys
sys.stdin = open('input1213.txt', encoding='utf-8')

for _ in range(10):
    tc = int(input())
    search_word = input()
    arr = input().count(search_word)

    print(f'#{tc} {arr}')