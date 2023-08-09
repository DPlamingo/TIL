import sys
sys.stdin = open('input3143.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split())

    cnt = 0 # 몇번 겹치는지 횟수를 세어줌
    text = '' # 빈 텍스트를 만들어 여기에 B의 첫째값을 A에서 뒤짐
    # 발견하면 B의 길이만큼 text에 A 발견한 뒤의 값을 추가
    k = 0
    for i in range(len(A)-len(B)+1):
        if k != 0:
            k -= 1
            continue

        if B[0] == A[i]:
            text = '' # text 리셋
            for j in range(len(B)):
                text += A[i+j]
            # print('---')
            # print(text)
            if B == text:
                cnt += 1
                k += len(B) -1
                # bananananananana nana
    # 횟수의 최소값은 전체 길이에서 겹치는 값을 빼주면됨
    # print(cnt)
    result = len(A) - (cnt*(len(B)-1))
    print(f'#{tc} {int(result)}')
