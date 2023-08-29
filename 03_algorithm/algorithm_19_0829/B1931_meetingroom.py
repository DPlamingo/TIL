# 회의실 배정

N = int(input())
meetingtime = [list(map(int, input().split())) for _ in range(N)]
rooms = []

meetingroom = [0] * (100000)

# print(meetingroom)

for start, end in meetingtime:  # 회의 시작, 끝 시간
    if start > end: #
        start,end = end,start
    for j in range(start,end):
        meetingroom[j] += 1

print(max(meetingroom)-1)