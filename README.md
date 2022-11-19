# Employess Project With Django

## Environment 

- Pycharm 에서 src를 Source Root로 지정할 것
- DataBase는 [DataBase](#DataBase) 참조
- `Makefile`을 이용해 자주 사용하는 command 이용

## Docker

- Command
    - `docker-compose up -d`

- Docker Compose
    - `nginx`
        - image: nginx:1.21.6-alpine
        - port: 8001
        - role: reverse proxy
    - `django`
        - image: python:3.8-buster
        - port: 3031
        - role: Source Deploy
        - Description
            - WSGI를 uWSGI를 사용

## Git Policy

- Command
    - `git config commit.template .gitmessage.txt`

- Commit Type
    - feat : 새로운 기능 추가
    - fix : 버그 수정
    - docs : 문서 수정
    - test : 테스트 코드 추가
    - refactor : 코드 리팩토링
    - style : 코드 의미에 영향을 주지 않는 변경사항
    - chore : 빌드 부분 혹은 패키지 매니저 수정사항

- Commit Template
    ```text
    <type> : <summary>
        # <type> : Commit Type에서 선택
        # <summary>: 형식으로 작성하며 제목은 최대 50글자 정도로만 입력
        
    # Description 
        # 제목 끝에 마침표 금지
        # 무엇을 했는지 명확하게 작성
  
    # Related Issue
        # 관련된 이슈 번호 작성
    ```

## DataBase

- `.devdbcontainer`
    - DB환경을 구성할 떄 위 디렉토리의 docker-compose를 이용할 것
- `Employees Structure`
    - `https://dev.mysql.com/doc/employee/en/sakila-structure.html`
    - `https://dataedo.com/samples/html/Employees_MySQL/doc/Employees_(MySQL_database)_7/tables.html`

---

# Policy

## Employees에 관한 노트

- `employee(s)` : 직원
    - 부서에 속해 있는 직원을 뜻한다. 다음과 같은 정보를 가진다.
        - 직원 번호, 생년월일, 성, 이름, 성별, 입사일
- `title(s)`: 직급
    - 직급은 다음과 같다.
        - Assistant Engineer, Engineer, Senior Engineer
        - Staff, Senior Staff
        - Technique Leader
        - Manager
    - 직원의 직급 정보를 기록한다.
    - 직원의 직급 정보가 변경된 경우 변경되기 전의 정보는 삭제되지 않는다.
- `salaries` : 급여
    - 직원의 연봉을 관리하며 년 단위로 직원의 연봉을 저장한다.
- `department(s)` : 부서
    - 직원은 하나의 부서에 속한다. 부서는 다음과 같은 정보로 구분된다.
        - 부서번호, 부서명