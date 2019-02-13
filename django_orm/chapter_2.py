# coding=utf-8
"""
task_2_1_p35 = task book, serial number, sub serial number, page book
"""
import os
import sys
import django


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config')
django.setup()

from django.db.models import (
    Q, F, Subquery, OuterRef, Value, Case, When, Func,
    IntegerField, CharField
)
from django.db.models.functions import Substr, Length, Concat

from django_orm.core.models import Emp


def task_1_p47():
    # select ename, job, sal from emp where deptno=10 order by sal asc;
    qs = (Emp.objects
          .filter(deptno=10)
          .order_by('sal')
          .values('ename', 'job', 'sal'))
    return qs


def task_1_1_p47():
    # select ename, job, sal from emp where deptno=10 order by sal desc;
    qs = (Emp.objects
          .filter(deptno=10)
          .order_by('-sal')
          .values('ename', 'job', 'sal'))
    return qs


def task_2_p48():
    # select * from emp where order by sal desc;
    qs = Emp.objects.order_by('deptno', '-sal')
    return qs


def task_3_p49():
    # select * from emp order by substr(job, length(job)-2);
    qs = (Emp.objects
          .annotate(sub_sort=Substr(F('job'),
                                    Length(F('job'), output_field=IntegerField())-2,
                                    output_field=CharField()))
          .order_by('sub_sort'))
    return qs


def task_4_p49():
    # select *, replace(
    #           translate(concat(ename, concat(' ', deptno)),
    #                     '0123456789', '##########'), '#', '') as sub_sort
    #   from emp order by sub_sort asc;
    qs = (Emp.objects
          .annotate(data=Concat('ename', Value(' '), 'deptno', output_field=CharField()),
                    sub_sort=Func(Func(F('data'),
                                       Value('0123456789'),
                                       Value('##########'),
                                       function='translate',
                                       output_field=CharField()),
                                  Value('#'),
                                  Value(''),
                                  function='replace',
                                  output_field=CharField()))
          .order_by('sub_sort'))
    return qs


def task_5_p53():
    # select *, case when comm is null then 0 else 1 end as sub_sort
    #   from emp order by sub_sort desc, comm asc;
    qs = (Emp.objects
          .annotate(sub_sort=Case(When(comm__isnull=True, then=Value(0)),
                                  default=Value(1),
                                  output_field=IntegerField()))
          .order_by('-sub_sort', 'comm'))
    return qs


def task_6_p60():
    # select * from emp order by case when job='salesman then comm else sal end asc;
    order_case = Case(When(job='SALESMAN', then=F('comm')),
                      default=F('sal'))
    qs = Emp.objects.order_by(order_case)
    return qs


if __name__ == '__main__':
    print(task_1_p47())
    print(task_1_1_p47())
    print(task_2_p48())
    print(task_3_p49())
    print(task_4_p49())
    print(task_5_p53())
    print(task_6_p60())
