# 뒤집기 백준 실버5 1439

# 넣고 끄집어 내면서 연속된것들 카운트

motion = input()
cnt0 = 0
# print(motion)
for i in range(len(motion)-1):
    if motion[i] != motion[i+1]:
        cnt0 += 1
        
print((cnt0+1)//2)

