import sys
sys.stdin = open('input1215.txt')

for tc in range(10):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(8)]


    # 회문을 설정해줌
    # 회문이 무엇인지
    cnt = 0
    range_arr = len(arr)-N+1
    if N == 1:
        cnt = 64

    for i in range(8):
        mid = N // 2
        if N % 2 == 0:
            for j in range(mid + 1):
                for k in range(1,(mid+1)//2+1):
                    if arr[i][j+mid-k+1] == arr[i][mid+j-k-1]:
                        continue
                    else:
                        break
                    cnt += 1
        else:
            for j in range(mid + 1):
                for k in range((mid + 1) // 2 ):
                    if arr[i][j + mid - k] == arr[i][mid + j + k]:
                        continue
                    else:
                        break
                    cnt += 1

    for i in range(8):
        mid = N // 2
        if N % 2 == 0:
            for j in range(mid + 1):
                for k in range(1, (mid + 1) // 2 + 1):
                    if arr[j + mid - k + 1][i] == arr[mid + j - k - 1][i]:
                        continue
                    else:
                        break
                    cnt += 1
        else:
            for j in range(mid + 1):
                for k in range((mid + 1) // 2):
                    if arr[j + mid - k][i] == arr[mid + j + k][i]:
                        continue
                    else:
                        break
                    cnt += 1


    print(f'#{tc+1} {cnt}')
