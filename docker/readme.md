# Deployment

## Content

- [Description](#Description)
- [init-db.sh](#init-db.sh)

---

## Description

- 개발에 필요한 DataBase 환경은 docker-compose를 이용해서 Setting한다.
    - `command`
        ```text
        $ sudo docker-compose up -d
        ```
- `docker-compose.yml`의 `port`를 변경해도 상관없으나 변경 시 `Django project config`도 변경 필요
- `DataBase` 접속 계정
    - `userid`: root
    - `password`: 1234

## init-db.sh

- `sample`로 제공되는 `schema`를 이용하기 때문에 `init-db.sh`를 이용해서 `schema`를 적용한다.  
