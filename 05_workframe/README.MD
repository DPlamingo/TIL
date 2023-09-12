# 시작하기 전 작성

## 프로젝트 관리
- TIL, 학습하고 있는 각종 폴더, 관통 PJT
- git으로 관리중
  - TIL/**/*.pt
  - git으로 관리 되지 않아야 할 목록
    - .gitignore : 가상환경 생성 (git으로 관리 x)

## 가상환경
- Python 애플리케이션과 그에 따른 패키지들을 격리하여 관리할 수 있는 독립적인 실행 환경
- git으로 관리 안한다. -> .gitignore
- local 작업할 때, 가상환경 안만들고, global에 django 설치하고 작업 진행하면,
매번 똑같은 환경에서 진행하는데 왜 필요할까?

### 가상환경 생성
```bash
# 항상 작업위치 확인하기.
# 파이썬아/ -m 모듈써서/ virtual enviroment 모듈써서 / venv라는 폴더에 가상환경 만들어줘
$ python -m venv { folder_name }
```

### 가상환경 실행
```bash
$ ls
{ venv folder_name }/
$ source { folder_name }/Scripts/Activate

```

## Django 설치
```bash
$ pip install django
```

### 다른 작업 환경을 위한 설정
```bash
# 현재 pip 목록을 얼린다.
$ pip freeze > requirements.txt

# requirements.txt 파일에 적힌 내용으로 설치
$ pip install -r requirements.txt

```

## Django 프로젝트 생성
```bash
# Django 프로젝트 
# offline 이름의 프로젝트
# 장고야 프로젝트 시작할 건데, offline이라는 이름으로 할 거야.
$ django-admin startproject offline
$ cd offline

# 현재 작업 위치에 프로젝트 생성
$ django-admin startproject offline .
```

### Django 서버 실행
```bash
$ python manage.py runserver
```

### Django App 생성 등록하기
```bash
# articles
$ python manage.py startapp articles
```
```python
# settings
INSTALEED_APPS = []
```

### articles app의 메인 페이지 화면에 띄우기
1. client가 요청 보낼 경로 지정하기 -> url
2. 특정 경로에 요청이 왔을때, 그 요청에 적절한 처리 하기(함수) -> views.py
3. 적절한 처리 과정에서 template(html)이 필요하다면, 작성하기 -> templates/*.html
4. 작성된 template을 사용자에게 반환하기 -> views에 정의한 함수의 return