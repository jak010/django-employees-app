import enum
import json

from django.http.response import HttpResponse


class EmployeeResponseCode(enum.Enum):
    OK = 200
    CREATED = 201
    NO_CONTENT = 204

    BAD_REQUEST = 400
    RESOURCE_ALREADY_EXISTS = 409

    SERVER_ERROR = 500


class EmployeeResponseContentType(enum.Enum):
    APPLICATION_JSON = "application/json"


class HttpEmployeeInvalidInputResponse(HttpResponse):
    status_code = EmployeeResponseCode.BAD_REQUEST.value
    content_type = EmployeeResponseContentType.APPLICATION_JSON.value

    def __init__(self):
        super(HttpEmployeeInvalidInputResponse, self).__init__(
            content=self._to_content,
            content_type=self.content_type
        )

    @property
    def _to_content(self):
        content = {
            "messages": "Invalid Input Request !",
            "error": {}
        }
        return json.dumps(content)