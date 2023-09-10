# 색종이 자르기 집에서

# 가장 폭 큰 값은
# x 축 맥스 길이 곱하기 y축 맥스 길이


paper = list(map(int, input().split()))
paper_wide = [[0]*paper[0] for _ in range(paper[1])]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

x = []
y = []
for i in range(N):
    if arr[i][0] == 1:
        x.append(arr[i][1])

    elif arr[i][0] == 0:
        y.append(arr[i][1])

x = sorted(x)
y = sorted(y)

x_cut = []
y_cut = []
for i in range(len(x)-1):
    x_cut.append(x[i+1]-x[i])
x_cut.append(paper[0]-x[-1])

for i in range(len(y)-1):
    y_cut.append(y[i+1]-y[i])
y_cut.append(paper[1]-y[-1])  

x_max = max(x_cut)
# print(x_max)
y_max = max(y_cut)
# print(y_max)
print(x_max*y_max)      