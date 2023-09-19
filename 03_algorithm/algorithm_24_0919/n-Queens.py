# n-Queens 문제

def n_queens(i,col): # i는 순서, col은 배열
    n = len(col) - 1
    if promising(i,col): # 유망하다면,
        if i == n: # 퀸 배치가 완벽하다면
            print(col[1: n+1]) # 배치 출력
        else:
            for j in range(1, n+1):
                col[i+1] = j
                n_queens(i+1, col) # 다음 배열 호출

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