# Control of flow
## 제어문
  - 반복에 따라 코드 실행, 조건에 따라 코드 블록 실행

## 조건문
  - 조건식을 만들면, 그것을 평가함 -> 참, 거짓 판별 후 실행하거나 건너 뜀
  
### if 문 (elif, else)
  1. if 문의 구조
    ```python
    if 표현식:
        코드 블록
    elif 표현식:
        코드 블록
    else:
        코드 블록
    ```

  2. 복수 조건문 예시
    - 조건식을 순차적으로 비교
    ```python
    dust = 480

    if dust > 150:
        print('매우 나쁨')
        if dust > 300: # 중첩 조건문
            print('위험해요! 나가지 마세요!')
    elif dust > 80:
        print('나쁨')
    elif dust > 30:
        print('보통')
    else:
        print('좋음')
       
    ```

## 반복문
  - 특정 작업을 반복적으로 수행, 특정 조건이 참인동안 반복

### for/while 문
  1. for 문
    - 종료 조건이 따로없고, 자체 종료 조건있음(임의의 시퀀스 항목, 개수가 있음)
    - 반복을 요소 순서대로 돔.

  2. 기본구조
    - for 변수 in 반복 가능한 객체(ex. list):
      코드 블록

  3. 반복 가능한 객체
    - 시퀀스, dic, set 반복 가능

  4. 중첩된 반복문 !! (2중 중첩된 반복문)
    - 바깥쪽 한번에 안쪽 반복이 끝나면 바깥쪽이 실행.

  5. 중첩 리스트 순회
    ```python
    elements = [['A', 'B'], ['c', 'd']]

    for elem in elements:
        for item in elem:
            print(item)
    
    ```

  6. while 문 (조건이 참(True)인 동안 계속 반복)
    - 주어진 조건식이 참인 동안 코드 반복 == 거짓이 될 때 까지 반복

  7. 기본구조
    - while 조건식:
          코드 블록

### 반복 제어
  1. break
    - 반복을 즉시 중지

  2. continue
    - 반복이 남아도 건너뜀
    
  3. continue 예시 !!

  4. break와 continue 주의 사항 
    - 남용하는 것은 코드의 가독성을 저하 시킬 수 있음.
    - 시간이 들더라도 코드의 가독성을 유지하고, 코드의 의도를 명확하게 작성하는게 중요.


### List Comprehension
  - 간결하고 효율적으로 리스트를 생성하는 방법.

  1. 기본구조
    - [expression for 변수 in iterable if 조건식]
      list(expression for 변수 in iterable if 조건식)

  2. 리스트를 생성하는 3가지 방법 비교
    - 어떤게 제일 빠른가
    - 정수 1, 2, 3을 가지는 새로운 리스트 만들기

    ```python
    numbers = ['1', '2', '3']
    # 1) for loop
      new_numbers = []
      for number in numbers:
          new_numbers.append(int(number))
      print(new_numbers)

    # 2) map
      new_numbers_2 = list(map(int, numbers))
      print(new_numbers_2)

    # 3) list comprehension
      new_numbers_3 = [int(number) for number in numbers]
      print(new_numbers_3)

    ```

### Pass
  - 아무런 동작없이 넘어가는 역할
  - 문법적으론 문장이 필요하짐나 실행시에는 영향을 주지 않아야 할 때.

### enumerate
  - 시퀀스를 반복할 때, index를 함께 호출해줌.

```python
result = ['a', 'b', 'c']

print(enumerate(result))
print(list(enumerate(result))) 

for index, elem in enumerate(result):
    print(index, elem)

```