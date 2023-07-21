# 함수와 제어문 1
## 함수
  - 특정 작업을 수행(목적) 하기 위해서 재사용 가능한 코드 묶음

1. 함수를 사용하는 이유
  - 사용했던 함수들을 재사용 하려는 이유가 큼

### 내장 함수
  - Built-in 되어 있는 것.(고정되어있는 것, import 필요없음)

1. 내장 함수 예시
  - 절대값을 만드는 함수

```python
result = abs(-1)
print(result) # 1
```

## 파이썬docs 
 - 배우는 수준으로는 1. Libray Ref.
                   2. Language Ref. 참고

2. 함수 호출
  - 함수를 실행한다

### 함수 구조
1. 함수 구조
  - 함수의 몸통 및 반환으로 구성.

```python
def make_sum(pram1, pram2): # <- 매개변수, def : 함수의 정의
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
                                                # 함수의 몸통 부분, 함수의 설명(Documentstring)
    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2 
    # 함수의 반환 값, return 아래의 코드는 죽은 값
```

### 매개변수와 인자(위치가 같음)
1. 매개변수
  - 함수를 정의할때, 함수가 받을 값을 나타내는 변수

2. 인자
  - 함수를 호출할 때, 실제 전달되는 값

3. 매개변수와 인자 예시
```python
def add_numbers(x, y): # x와 y는 매개변수

a = 2
b = 3
sum_result = add_numbers(a, b) # a와 b는 인자
print(sum_result)

```

### 인자의 종류
1. 위치인자
  - 인자의 위치에 따라 달라짐

2. 기본 인자 값
  - 입력하지 않으면, 기본 값으로 설정되는 것.

3. 키워드 인자
  - 함수 호출 시, 인자의 이름과 함께 값을 전달 함.

4. 함수 인자 권장 작성순서
  - 위치 -> 기본 -> 가변 -> 가변 키워드


### 함수와 Scope
1. Python의 범위
  - Global scope : 코드 어디에서든 참조할 수 있는 공간
  - Local scope : 함수가 만든 scope (함수 내부에서만 참조 가능)
  ```python
  def my_func():
      num = 1 # 들여쓰기로, num의 scope가 다름
  print(num) # num 인식이 안됨
  ```

2. 변수 수명주기 
  1. built-in scope
    - 파이썬이 실행된 이후부터 영원히 유지
  2. global scope
    - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
  3. local scope
    - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

3. 이름 검색 규칙(LEGB Rule) !!
  - Built-in > Global > Enclosed > Local
  - 하위에서 없으면 위로 찾으러 올라감.

4. 'global' 키워드
  - 함수 내에서 전역 변수를 수정하려는 경우


### 재귀 함수 !!
  - 함수내에서 자기 자신을 호출하는 함수
  - 무한 호출 유의
  - 종료 조건을 명확히 제시
  - 반복되는 호출이 종료 조건을 향하도록 만들어야함

1. 재귀 함수 예시 - 팩토리얼
  - n! -> f(n) = n * f(n-1)
  - n-1! -> f(n-1) = n * f(n-2) ....
```python 
def factorial(n):
    # 종료 조건 : n이 0이면 1을 반환
    if n == 0
        return 1
    # 재귀 호출 : n과 n-1의 팩토리얼을 곱한 결과를 반환
    return n * factorial(n-1)

# 팩토리얼 계산 예시
result = factorial(5)
print(result) # 120

```

### 유용한 내장함수
1. map(function, iterable) [interable : 반복하능한 객체(문자열)]
```python
numbers = [1, 2, 3]
result = map(str, numbers)

print(result) # <map object at 0x000001B5C0B>
print(list(result)) # ['1', '2', '3']

result = []
for number in numbers:
    result.append(str(number))
```

2. zip(*iterables)
  - 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

3. lambda 함수 (남용 x)
  - 이름이 없는 함수
  1. lambda 함수 구조
    - lambda 매개변수 : 표현식
  2. 예시
    ```python
    addition = lambda x, y : x + y
    result = addition(3, 5)
    print(result) # 8

    # map + lambda
    numbers = [1, 2, 3, 4, 5] # 다 2배의 값으로 만들고 싶다.
    result = list(map(lambda x: x * 2, numbers))
    print(result) # [2, 4, 6, 8, 10] , 일회성

    
    numbers = [
      {'가' : 30, '나' : 135, '다' : 30},
    {'가' : 40, '나' : 35, '다' : 20},
    {'가' : 50, '나' : 5, '다' : 30},
    {'가' : 20, '나' : 525, '다' : 40}
    ]
    ```


## Packing & Unpacking
### Packing (잘 사용 안함) !!
1. 패킹 예시
  - 변수에 담긴 값들은 tuple 형태로 묶임
```python
packed_values = 1, 2, 3, 4, 5
print(packed_values) # (1, 2, 3, 4, 5)
```

2. '*'을 활용한 패킹
```python
numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers

print(a) # 1
print(b) # [2, 3, 4]
print(c) # 5
```

### Unpacking (자주 사용)!!
1. 언패킹 예시
```python
packed_values = 1, 2, 3, 4, 5
a, b, c, d, e = packed_values

print(a, b, c, d, e) # 1 2 3 4 5
```


## Module
  - 한 파일을 만들면, 그것이 모듈이 됨

1. 패키지
  - 모듈을 모아 놓은 곳
```python
from my_package.math

```


