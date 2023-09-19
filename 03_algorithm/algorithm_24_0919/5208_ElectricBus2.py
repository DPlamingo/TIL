# 전기버스 2

T = int(input())
for tc in range(1, 1+T):
    battery = map(int,input().split())
    col = [0] * (len(battery)+1)
    for i in range(1,len(col)):
        col[i] += battery[i-1]

    idx = 1
    cnt = 0
    while len(battery) - idx > col[idx]:
        cnt += 1
        idx += 1


def electric_bus(i,col): # i는 순서, col은 배열
    n = len(col) - 1
    if promising(i,col): # 유망하다면,
        if i == n: # 버스가 끝에 도착했다면
            print(col[1: n+1]) # 배치 출력
        else:
            for j in range(1, n+1):
                col[i+1] = j
                electric_bus(i+1, col) # 다음 배열 호출

def promising(i, col):
    k = 1
    flag = True # 유망한지 확인,
    while k<i and flag: # k가 열임
        if col[i] == col[k] or abs(col[i] - col[k]) == i-k:
            flag = False
        k += 1
    return flag # 플래그가 True로 된다면 완벽

n = 5
col = [0] * (n+1)
n_queens(0, col)