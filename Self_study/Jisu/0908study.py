# 백준 실1 숨박꼭질

start, end = map(int, input().split())

queue = [[start]] # 시작
cnt = 0 # 초
switch = 1 
if start == end:
    print(0)
    exit()
while True:
    cnt += 1 # 1초가 지남
    node = queue.pop(0) # 큐 처음값이 노드임
    # print(node)
    queue2 = [] # 임시 큐
    for i in node: # 노드 리스트 처음부터 계산
        if i == end:
            print(cnt)
            exit()
        if 0 <= i+1 <= 100000 and i+1 not in node:
            queue2.append(i+1) 
    

        if 0 <= i-1 <= 100000 and i-1 not in node:
            queue2.append(i-1)
            

        if 0 <= 2*i <= 100000 and 2*i not in node:
            queue2.append(2*i)

    queue.append(queue2)

