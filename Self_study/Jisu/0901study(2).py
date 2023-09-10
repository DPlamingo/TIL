# 백준 약수의 합



n = int(input())

nums = []
for i in range(1,n):
    if n%(i) == 0:
        nums.append(i)
# print(nums)
if sum(nums) != n:
    print(f'{n} is NOT perfect.')
else:
    print(f'{n} = ',end='')
    for i in nums:
        if i != nums[-1]:
            print(i,'+ ',end='')
        else:
            print(i)
