import sys
sys.stdin = open('inputextra_pari_kill.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input(). split())) for _ in range(N)]

    # 자 시작하기 전에, 무엇을 해야될까
    # 일단 도화지가 있는데 크기가 M x M 구역에 대한 값을 다더해야됨
    # 왜 why? 파리채의 크기임 그 범위만큼 잡은 값이 다더한거임
    # 결국 파리채의 index를 준 값으로 그 구역을 복사하자
    # 파리채의 크기
    # 기준이 i라면 파리채 y축은 i+M+1 가 범위임
    # 기준이 j라면 파리채 x축은 j+M+1 가 범위임
    # 하지만 i+M+1 < N보다 작아야함 범위안에 드가야하니까

    max_kill = []

    for i in range(N-M+1): # y축 범위가 나옴
        for j in range(N-M+1): # x축 범위가 나옴
            list_pari = [] # 파리채 리스트를 만듬
            for k in range(i,i+M): # 파리채 y축 공간
                for l in range(j,j+M): # 파리채 x축 공간
                    list_pari.append(arr[k][l]) # 파리채 리스트에 공간의 값 다넣음 리스트 값으로
            # print(list_pari)
            max_kill.append(sum(list_pari)) # 돌기전에 그 값들 합을 따로 킬리스트로 새로 만듬

    print(f'#{tc} {max(max_kill)}') # 킬 리스트 모음중에서 맥스값
