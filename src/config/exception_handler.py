from __future__ import annotations

from rest_framework.response import Response

# from rest_framework.views import exception_handler

from rest_framework.exceptions import APIException
from rest_framework import exceptions as drf_exceptions

from .exceptions import (
    BadRequestError, NotFoundError
)

from . import exceptions as define_exec


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
        # custom exceptions
        if isinstance(self._errors, define_exec.NotFoundError):
            exec = NotFoundError()

        # DRF Exceptions:
        if isinstance(self._errors, drf_exceptions.ValidationError):
            exec = self._errors

        # Response Object
        self.response.status_code = exec.status_code
        self.response.data = {
            'code': exec.default_code,
            'debug': exec.detail,
        }

# def exception_handler_func(exc, context):
#     print("="*20)
#     print(exc, context, type(exc), type(context))
#     print("=" * 20)
#     exec = ""
#     if isinstance(exc, ValidationError):
#         exec = BadRequestError()
#     if isinstance(exc, NotFoundError):
#         exec = NotFoundError()
#
#     response = exception_handler(exec, context)
#     if response is not None:
#         response.data['code'] = exec.get_codes()
#         response.data['detail'] = exc.get_full_details()
#
#     return response
