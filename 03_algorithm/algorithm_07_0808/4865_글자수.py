import sys
sys.stdin = open('input4865.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    cnt = 0 # 빈카운트를
    list_cnt = [] # 리스트에 넣어서 정리
    for i in range(len(str1)):
        cnt = 0 # 리셋
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt += 1
        list_cnt.append(cnt) # 뒤에 놔둬도 갯수차이로 됨.

    def max_fuction(arr):
        if len(arr) == 1:
            arr = arr[0]
        max = arr[0]
        for num in arr:
            if(max<num):
                max=num
        return max


    result = max_fuction(list_cnt)
    print(f'#{tc} {result}')