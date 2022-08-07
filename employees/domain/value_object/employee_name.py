from __future__ import annotations


class EmployeeName:
    def __init__(self, last_name: str, first_name: str):
        self._last_name: str = last_name
        self._first_name: str = first_name

    def __eq__(self, other: EmployeeName):
        if not isinstance(other, EmployeeName):
            raise Exception("other is not instance of EmployeeName")

        if (self._last_name == other._last_name) == (self._first_name == other._first_name):
            return True
        return False

    def __hash__(self):
        return hash(self._first_name + self._last_name)
