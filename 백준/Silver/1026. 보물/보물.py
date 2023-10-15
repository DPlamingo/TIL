# 1026. 보물4 백준

# S = A[i] * B[i] for i in range(N)

# S의 최솟값은?
# A는 재배열 가능, B는 안됨
# 최소는 결국 A 작은값들과 B 큰값들 서로 곱하면됨
# 어차피 값만 나오는거니 둘다 배열 역배열로 곱함
# 안된다했을땐, B 역배열하고 그에 맞는 인덱스에
# A값 순서대로 주르륵 곱하면됨

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

S = 0
for i in range(N):
    S += A[i]*B[i]

print(S)
