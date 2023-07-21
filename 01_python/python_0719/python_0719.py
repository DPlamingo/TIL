def func_name(parm1, parm2):

    return parm1 + parm2

func_name(1, 2) # 함수를 호출 한 것
# 함수를 호출하는 행위 -> 평가 후 값을 내는 표현식
print(func_name(1, 2)) # 3


def greeting(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요!')

# 모든 매개 변수에 키워드 인자 형식으로 값을 넘겼을 때.
greeting(age = 30, name = '홍길동')
# greeting(age = 30, '홍길동')
# 함수가 끝났기 때문에 return none 호출만 됨.

print('첫', '두', '세', end='\t', sep=':')
print('다음 줄')

# 가변인자로 매개변수를 정의하면
# 함수를 호출 할 때, N개의 값을 넘겨도 모두 하나의 변수에 할당
# 이때, tuple 형태로 할당 된다.

def func(*args, sep=' '):
    print(args, sep)

func('첫', '두', '세')


# Scope
numbers = [1, 2, 3]
age = 100 # global scope (.py 파일하나로 잡음)

def parent_func(name): # en-closed
    age = 30

    def child_func(child_name): # local
        age = 20
        numbers[2] = 1000
        print(age, 'child_func')        
    
    child_func()
    print(age, 'parent_func')

parent_func()
print(age, 'global')
print(numbers)


global_var = '글로벌 값'

def update_value(global_var): # 매개 변수 -> local scope
    print(global_var, '매개 변수로 받은 값')
    result = global_var * 3 # 글로벌 변수가 가지고 있던 값 활용 가능
    global_var = '로컬 값' # 글로벌 변수에 할당된 값에 영향 없이 다른값 재할당 가능

    return result
# 애초에 안되게 하지 왜 되게해서 헷갈리게 하나요?
# 1. 막아 놔있음.
# 2. 코드는 작성자 본인이 작성, 규칙에만 맞춰서 잘 쓰는 편하게 사용 할 수 있다.

print(update_value(global_var)) # 인자로 global scope 변수를 넘김
print(global_var)


def factorial(n):
    # 종료 조건 : n이 0이면 1을 반환
    if n == 0:
        return 1
    # 재귀 호출 : n과 n-1의 팩토리얼을 곱한 결과를 반환
    return n * factorial(n - 1)

# 팩토리얼 계산 예시
result = factorial(5)
print(result) # 120


def some_func(parm1):
    return parm1 ** 2

print(some_func(1, 2))
print(some_func)

other_var = some_func
print(other_var(1, 2))
numbers = [1, 2]
print(list(map(other_var, numbers)))

def my_map(func, iterable):
    for item in iterable:
        resule = func(item)
        print(result, end=' ')

my_map(some_func, numbers)


# '10 9 120'
# input().split() -> ['10', '9', '120']
# int('10')
# int('9')
# int('120')
# <map [10, 9, 120]>
# N, K, M = map(int, input().split())
# N = 10
# K = 9
# M = 120
data = list(map(int, input().split()))
N, K, M = map(int, input().split())

print(data)
print(N, K, M)


# 모듈
import random

random.shuffle

# import quetion

# my_func = quetion.func_name
# print(my_func(1, 2))

import requests

url = 'https://random-data-api.com/api/v2/users'
response = requests.get(url).json()
print(response)

# pip install django


# from recur import factorial
# from question_2 import func_name as que_2_func
# from quetion import func_name
