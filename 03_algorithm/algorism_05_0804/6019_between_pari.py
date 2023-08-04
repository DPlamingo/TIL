import sys
sys.stdin = open('input6019.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    # D 값은 위치
    # A 는 A 속력
    # B 는 -B 속력
    # F 는 파리의 속력
    # A가 멈춰있다고 보면 B의 속력은 -B-A
    # 파리의 속력은 F-A
    # B는 250지점에서 출발, 파리와 출돌하면 파리 A쪽으로감
    # B가 A에게 출동할 시간 h = D/abs(-B-A) : 10시간
    # 근데, h동안 파리가 같은 속도로 가기때문에 F*h하면 답나옴

    D = arr[0] # 거리
    A = arr[1] # A의 속력
    B = arr[2] # B의 속력
    F = arr[3] # 파리의 속력

    H = D/abs(-B-A) # 충돌할때 걸리는 시간
    result = F*H # 파리가 충돌할때까지 걸린 시간

    print(f'#{tc} {result}')