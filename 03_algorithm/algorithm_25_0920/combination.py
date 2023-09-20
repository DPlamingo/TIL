
arr = [1, 3, 2, 4, 5]

# 이거 모든 조합의 경우 출력해보셈

count = 0
for i in range(2):
    for j in range(2):
        for k in range(2):
            for m in range(2):
                for n in range(2):
                    bit = [0, 0, 0, 0, 0]

                    if i:
                        bit[0] = arr[0]
                    if j:
                        bit[1] = arr[1]
                    if k:
                        bit[2] = arr[2]
                    if m:
                        bit[3] = arr[3]
                    if n:
                        bit[4] = arr[4]
                    count += 1

                    for gg in bit:
                    print(bit)

print(count)