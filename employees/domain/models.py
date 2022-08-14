from __future__ import annotations

from django.db import models

from django.db.models import Manager

# Create your models here.

from typing import TypeVar

DjangoModelType = TypeVar('DjangoModelType', bound=models.Model)


class Employees(DjangoModelType):
    class Meta:
        db_table = 'employees'

    emp_no = models.IntegerField(primary_key=True)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1)
    hire_date = models.DateField()

    objects = Manager()


class Titles(models.Model):
    emp_no = models.ForeignKey(Employees, models.DO_NOTHING, db_column='emp_no', primary_key=True)
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titles'
        unique_together = (('emp_no', 'title', 'from_date'),)
