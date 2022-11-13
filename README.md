# Employess Project With Django

## Config
- Pycharm 에서 src를 Source Root로 지정할 것 
- .gitmesasge.txt -> `git config commit.template` 으로 지정할 것


# Git Commit Message
```text
# .git-commit-rule.txt

# <타입> : <제목> 형식으로 작성하며 제목은 최대 50글자 정도로만 입력
# 제목을 아랫줄에 작성, 제목 끝에 마침표 금지, 무엇을 했는지 명확하게 작성

################
# 본문(추가 설명)을 아랫줄에 작성

################
# 꼬릿말(footer)을 아랫줄에 작성 (관련된 이슈 번호 등 추가)

################
# feature : 새로운 기능 추가
# fix : 버그 수정
# docs : 문서 수정
# test : 테스트 코드 추가
# refactor : 코드 리팩토링
# style : 코드 의미에 영향을 주지 않는 변경사항
# chore : 빌드 부분 혹은 패키지 매니저 수정사항
################
```

# Employees에 관한 노트

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

# Points

- containerized 적용해보기
- 최대한 django module을 이용해서 구현해보기
- typing 적용하기
- domain 언어로 표현해보기
    - domain 언어 : value object, entity, service, repository


# Reference

- `Employees Structure`
    - `https://dev.mysql.com/doc/employee/en/sakila-structure.html`
    - `https://dataedo.com/samples/html/Employees_MySQL/doc/Employees_(MySQL_database)_7/tables.html`