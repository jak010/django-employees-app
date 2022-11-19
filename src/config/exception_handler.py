from __future__ import annotations

from rest_framework import exceptions as drf_exceptions
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from . import exceptions as define_exec
from .exceptions import (
    NotFoundError
)


# from rest_framework.views import exception_handler


class ExceptionMeta(type):

    def __init__(cls, *args):
        type.__init__(cls, *args)

    def __call__(cls, *args, **kwargs):
        exception_handler: ExceptionHandler = type.__call__(cls, *args, **kwargs)
        exception_handler.exceptions_checker()

        return exception_handler.response


class ExceptionHandler(metaclass=ExceptionMeta):
    def __init__(self, *args, **kwargs):
        self._errors: APIException = args[0]
        self._view = args[0:]

        self.response: Response = Response()

    def exceptions_checker(self):
        _exec = None
        # custom exceptions
        if isinstance(self._errors, define_exec.NotFoundError):
            _exec = NotFoundError()

        # DRF Exceptions:
        if isinstance(self._errors, drf_exceptions.ValidationError):
            print("3" * 20)
            _exec = self._errors

        # API Exception
        if issubclass(type(self._errors), APIException):
            # Response Object
            self.response.status_code = self._errors.status_code
            self.response.data = {
                'code': self._errors.default_code,
                'debug': self._errors.detail,
            }
        else:
            # Internal ServerError
            raise self._errors
