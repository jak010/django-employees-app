# Employees API

### Employee 생성

> Method :  POST
> URL : employee/create

### Request

- `emp_no` : int
- `first_name` : str
- `last_name` : str
- `gender` : Optional['M','F']
- `birth_date` :date
- `hired_date` : date

### Response

- `201 Created` : Employee 생성에 성공함
  ```json 
  {
      "message": "Employee Was Created!",
      "data": {
          "emp_no": 2,
          "first_name": "k",
          "last_name": "j",
          "gender": "M",
          "birth_date": "2022-08-21",
          "hire_date": "2022-08-21"
      }
  }
  ```

- `409 Conflict` : 이미 존재하는 Employee
   ```json
    {
        "message": "Already Exist Employee !",
        "data": {}
    }
    ````
