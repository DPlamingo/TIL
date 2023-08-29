N = int(input())
meetingtime = [list(map(int, input().split())) for _ in range(N)]
rooms = []

arr = []
for start, end in meetingtime:
    if start > end:
        start,end = end,start
    arr2 = [range(start,end)]
arr.append(arr2)

for i in range(len(arr)):

