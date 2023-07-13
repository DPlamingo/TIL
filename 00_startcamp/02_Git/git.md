# GIT 이란...
> 분산 버전 관리 시스템
- 분산 : 퍼트리는 것
- 버전 : 버전(어떤 변화를 기록하는 것)
    - 왜? 잘못 됬을때 알아야됨, 처음부터 다시하지 않기 위해서

- 관리 : 관리
- 시스템 : 시스템
- 버전 관리 : 변화를 기록하고 추적하는 것
* GIT : 코드의 '변경 이력'을 기록하고 '협업'을 원활하게 하는 도구

## 중앙 VS 분산
- 중앙 집중식 : 버전은 중앙 서버에 저장되고 중앙 서버에서 파일을 가져와 다시 중앙에 업로드
    - 단점 : 물리적으로 데이터 손실시 복구 어려움 (토이스토리 썰)
- 분산식 : 버전을 여러 개의 복제된 저장소에 저장 및 관리 (Git Lab, Git Hub)
    - Git Lab : 개인용
    - Git Hub : 싸피용

## Git의 역할
- 코드의 버전(히스토리)를 관리
- 개발되어 온 과정 파악
- 이전 버전과의 변경 사항 비교

### Git의 3가지 역할
1. Working Directory (Git과 크게 연관 없음, Git이 바라만 보고 있는 역할)
    - 실제 작업 영역
2. Staging Area
    - Working Directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
3. Repository
    - 버전 이력과 파일들이 영구적으로 저장되는 영역
    - 모든 버전과 변경 이력이 기록됨

    3.1 Loacl
        - Git폴더 자체


    3.2 Remote
        - 집~강의실을 연결해 주는 다리 (ex.git hub, git lab)

### Git 초기화
```bash
$ git init
```

- Commit : 변경된 파일을 저장하는 행위
- No commits yet : 버전 변경이 없음

### 상태 확인 명령어
```bash
$ git status
`````

### git 초기화
```bash
$ git init
```
- Initialized empty Git repository in C:/Users/SSAFY/Desktop/new_folder/.git/ => 여기에 git이 있다.
- git 위치의 동/하위 폴더들을 다 관리한다. (바깥쪽은 관리X)
- SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/new_folder (master) => master라는 애가 관리하고 있다.
- 하위폴더에 init 가능하긴 하지만 우리는 안할거임
- windows>자격증명 관리> windows 자격 증명> 일반 자격증명 > git깔려있으면 자동로그인
- 숨김폴더 보려면 

```bash
$ ls -a #all
```
### commit
- 변경된 파일 저장하는 행위
- 상태 확인 명령어
```bash
$ git status
```

### staging area에 추가 (W->S)
```bash
$ git add {path}<folder_name>/{file_name}
```

###
```bash
$ git rm
```

### 사용자 지정
- git config --global user.email "you@example.com"
- git config --global user.name "Your Name"

### Repository에 저장하기
```bash
$ git commit -m "commit messsage" # message(버전) #commit message는 자세할수록 좋다.
```

### git 기초설정
```bash
$ git config --global user.email "kyb1434@gmail.com"
$ git config --global user.name "김연빈"

$ git config --global --list

#terminal 복사는 우클릭, shift+insert: 붙여넣기, ctrl+c 는 실행취소
```

### checking commit log
```bash
$ git log #이때 나오는 숫자들이 커밋을 식별하게 해주는 거
```

### 직전 커밋 수정
```bash
$ git commit --amend 
#vi / vim 으로 넘어감 (메모장) - 환경자체를 건드림
# 1. 'insert' 눌러서 수정가능상태로 바꾸기 > 커밋 메시지 수정
# 2. 'esc' 눌러서 삽입상태 종료
# 3. ':wq'입력 후 저장하고 종료 (write quit)
```

### git 설정 초기화
```bash
# 'insert' key 수종 상태 만들기
# vim을 활용해서 설정 제거하기 (Ctrl + U)
# 저장하기 (ESC key)
# 종료하기 (:wq)
# vim git 설정 파일 열기
$ vim ~/.gifconfig
```
```bash
$ code ~/.gifconfig
# vs코드로 충분함
```

### git config 상태에서 지우면 안될파일등을 지웠을때
```bash
# 'ESC' key를 눌러 입력 상태종료
# 'w' key를 눌러 실행취소
```

### 원격 저장소
- Git Lab (SSAFY 공식)
- Git Hub (Open소스, Public)
- Bitbucket
