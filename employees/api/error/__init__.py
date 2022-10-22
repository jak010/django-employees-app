from enum import Enum, unique
import json

from django.http.response import HttpResponse


@unique
class EmployeeResponseErrorCode(Enum):
    EMPLOYEE_DUPLICATE_CODE = 10001


class BaseEmployeeError(HttpResponse):

    def __init__(self):
        super().__init__(
            content=self.to_content,
            content_type="application/json"
        )

    @property
    def to_content(self):
        raise NotImplementedError()
