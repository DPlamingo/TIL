# 요격 시스템

target = input()
print(target)
temp = []
for i in target:
    if i.isnumeric():
        temp.append(int(i))
print(temp)

targets = []


for i in range(0,len(temp),2):
    temp2 = []
    for j in range(2):
        print(temp)
        if i+j < len(temp):
            temp2.append(temp[i+j])
            print(temp2)
    targets.append(temp2)
print(targets,'target2')

targets.sort(key=lambda x:x[1])
print(targets,'targets')
# while targets:
#     s, e = targets[0][0], targets[0][1]


