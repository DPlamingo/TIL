# IM 대비용 백준

# 개미가 대칭점으로 가서 벽 부딪힐때마다 위치 바뀜

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())


if w < (p+t)%(2*w) < 2*w:
    p = (2*w) - (p+t)%(2*w)
else:
    p = (p+t)%(2*w)


if h < (q+t)%(2*h) < 2*h:
    q = (2*h) - (q+t)%(2*h)
else:
    q = (q+t)%(2*h)
print(p, q)