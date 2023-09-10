# 백준 브1 소인수분해
import sys
# print = sys.stdout.write

N = int(sys.stdin.readline())

cnt = 2
soinsu = []
while cnt != N:
    if N % cnt == 0:
        soinsu.append(cnt)
        N = N//cnt
    else:
        cnt += 1

s = ''
soinsu.append(N)
for i in soinsu:
    s += str(i) + '\n'
sys.stdout.write(s)
