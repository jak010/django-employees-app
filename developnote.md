
- `2022.08.14` : `Employees`와 `title`
  - `python manage.py inspectdb`로 models 정보를 불러왔을 때 `employees`와 `title`는 one-to-one 관계를 맺는다 정의되었다.
  - 하지만 `titles` 쪽에서 생성된 데이터를 보면 employees와 1:1 관계를 맺는 것이 아니라 여러 데이터를 가지는 걸 확인할 수 있다.
---