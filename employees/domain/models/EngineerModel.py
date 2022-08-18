from __future__ import annotations

from django.db import models

from .models import Employees


class EngineerManager(models.Manager):
    """ Engineer만 추출하는 Employees의 Proxy Model """

    def get_queryset(self):
        # select_related가 사용된 것에 주목하라
        return super(EngineerManager, self).get_queryset() \
            .select_related('titles').filter(titles__title='Engineer')


class Engineer(Employees):
    objects = EngineerManager()

    class Meta:
        proxy = True
