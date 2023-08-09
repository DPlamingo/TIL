import sys
sys.stdin = open('input1213.txt', encoding='utf-8')

for _ in range(10):
    tc = int(input())
    # print(tc)
    search_word = input()
    # print(search_word)
    arr = input()
    # print(arr)

    debug_word = ''
    cnt = 0
    for i in range(len(search_word)):
        for j in range(len(arr)-len(search_word)+1):
            if search_word[i] == arr[j]:
                debug_word = ''
                for k in range(len(search_word)):
                    debug_word += arr[j+k]
                # print(debug_word)
                # print('===')
                if debug_word == search_word:
                    cnt += 1

    print(f'#{tc} {cnt}')