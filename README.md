# Employess Project With Django

# Employees에 관한 노트

- `employee(s)` : 직원
    - 부서에 속해 있는 직원을 뜻한다. 다음과 같은 정보를 가진다.
        - 직원 번호, 생년월일, 성, 이름, 성별, 입사일
- `title(s)`: 직급
    - 직원은 최소한 하나의 직급이 존재하며 두 개 이상의 직급을 가질 수 있다.
    - 직급은 다음과 같다.
        - Engineer, Assistant Engineer, Senior Engineer
        - Staff, Senior Staff
        - Technique Leader
        - Manager
- `salaries` : 급여
    - 직원의 연봉을 관리하며 년 단위로 직원의 연봉을 저장한다.
- `department(s)` : 부서
    - 직원은 하나의 부서에 속한다. 부서는 다음과 같은 정보로 구분된다.
        - 부서번호, 부서명

# Reference

- `Employees Structure`
    - `https://dev.mysql.com/doc/employee/en/sakila-structure.html` 