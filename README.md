# Employess Project With Django

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