from __future__ import annotations

import json

from employees.api.error import EmployeeResponseErrorCode, BaseEmployeeError


class DuplicateEmployeeResponseError(BaseEmployeeError):
    """ 중복된 Employee 정보 """

    @property
    def to_content(self):
        to_content = {
            "ErrorCode": EmployeeResponseErrorCode.EMPLOYEE_DUPLICATE_CODE.value,
            "message": "Already Exist Employee !"
        }
        return json.dumps(to_content, default=str, indent=4)
