# 조건문
num = int(input('숫자를 입력하세요 : '))

# list -> sequence type 데이터 : 순서가 있따.
# list -> 길이를 알 수 있다. len(list)
# range -> 0 ~ n-1 까지의 숫자 범위를 만들 수 있다.
# range -> sequence type, iterable
# for 특성 | iterable 한 값이 가지고 있는 각 요소들을,
            # 임시 변수에 할당해서 코드를 실행
# for 문으로 range를 순회하면, range가 가지고 있는 0부터 n-1 까지의 값을 순회

print(list(range(3)) # [0, 1, 2]

for index in range(3):
    print(index)


dusts = [60, 50, 66, 70]
print(len(dusts)) #4
print(range(len(dusts))) # range(0, 4) -> 0, 1, 2, 3 ; 출력하고 싶은 위치 조정가능
for index in range(len(dusts)):
    print(dusts[index])

        
dusts = [60, 50, 66, 70]
for index in range(len(dusts)):
    dusts[index] = 0

print(dusts)




# if statement
# num이 홀수라면 (2로 나눈 나머지가 1이라면)
if num % 2 == 1:
# if num % 2: # 1은 true 로 평가됨.
    print('홀수입니다.')
# num이 홀수가 아니라면(짝수면)
else:
    print('짝수입니다.')
===


# while statement
a = 0

while a < 3:
    print(a)
    a += 1

print('끝')


# List Comprehesion
# 0~9 요소를 가지는 리스트 만들기
new_list = []
for i in range(10):
    if i % 2 == 1:
        new_list.append(i) 
print(new_list)

# 간결
new_list_2 = [i for i in range(10) if i % 2 == 1]
new_list_3 = [i for i % 2 == 1 else str(i) for i in range(10)] # elif 안됨.
print(new_list_2) # [1, 3, 5, 7, 9]
print(new_list_3) # ['0', 1, '2', 3, '4', 5, '6', 7, '8', 9]

# 프로그래밍 : 우리 프로그램이 어떻게 그 목적을 명확하게 전달하는지에 대한 것.
# '작은 효율성에 대해서는, 말하자면 97% 정도에 대해서는, 잊어버려라. 섣부른 최적화는 모든 악의 근원이다. -도널드 knuth