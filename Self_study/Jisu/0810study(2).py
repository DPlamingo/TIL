# IM 대비용 일곱 난쟁이

import sys
sys.stdin = open('input0810study(2).txt')

list_input = []
for i in range(9):
    list_input.append(int(input()))


for i in range(1 << len(list_input)):
    list_short = []
    for j in range(len(list_input)):
        if i & (1<<j):
            list_short.append(list_input[j])
            
            if sum(list_short) == 100 and len(list_short) == 7:
                result = sorted(list_short)
                for i in result:
                    print(i)



