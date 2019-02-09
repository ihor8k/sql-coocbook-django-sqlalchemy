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
    Q, F, Subquery, OuterRef, Value, Case, When,
    IntegerField, CharField
)
from django.db.models.functions import Concat, Coalesce

from django_orm.core.models import Emp


def task_1_p33():
    # select * from emp where deptno=10
    qs = Emp.objects.filter(deptno=10)
    return qs


def task_2_p34():
    # select * from emp
    # where deptno=10 or
    #       comm is not null or
    #       sal<=2000 and
    #       deptno=20;
    qs = Emp.objects.filter(
        Q(deptno=10) |
        Q(comm__isnull=False) |
        Q(sal__lte=2000) &
        Q(deptno=20)
    )
    return qs


def task_2_1_p35():
    # select * from emp
    # where (deptno=10 or
    #        comm is not null or
    #        sal<=2000) and
    #       deptno=20;
    qs = Emp.objects.filter(
        (Q(deptno=10) |
         Q(comm__isnull=False) |
         Q(sal__lte=2000)) &
        Q(deptno=20)
    )
    return qs


def task_3_p35():
    # select ename, deptno, sal from emp;
    qs = Emp.objects.values('ename', 'deptno', 'sal')
    return qs


def task_4_p36():
    # select sal as salary, comm as commission from emp;
    qs = (Emp.objects
          .annotate(salary=F('sal'), commission=F('comm'))
          .values('salary', 'commission'))
    return qs


def task_5_p37():
    # TODO later to review and restructure, a bit not so
    # select * from (select sal as salary, comm as commission from emp) x where salary<5000;
    sbqs = (Emp.objects
            .filter(empno=OuterRef('empno'))
            .annotate(salary=F('sal'))
            .values('salary'))
    qs = (Emp.objects
          .annotate(salary=Subquery(sbqs, output_field=IntegerField()))
          .filter(salary__lt=5000))
    return qs


def task_6_p38():
    # select ename || ' WORK AS A ' || job as msg from emp where deptno=10;
    qs = (Emp.objects
          .annotate(msg=Concat('ename', Value(' WORK AS A '), 'job'))
          .filter(deptno=10)
          .values('msg'))
    return qs


def task_7_p39():
    # select sal, ename,
    #        case when sal <= 2000 then 'underpaid'
    #             when sal >= 4000 then 'overpaid'
    #             else 'ok'
    #        end as status
    #   from emp;
    qs = (Emp.objects
          .annotate(status=Case(When(sal__lte=2000, then=Value('underpaid')),
                                When(sal__gte=4000, then=Value('overpaid')),
                                default=Value('ok'),
                                output_field=CharField(max_length=24)))
          .values('status', 'sal', 'ename'))
    return qs


def task_8_p40():
    # select * from emp limit 5;
    qs = Emp.objects.all()[:5]
    return qs


def task_9_p42():
    # pstgresql
    # select * from emp order by random() asc  limit 5;
    qs = Emp.objects.order_by('?')[:5]
    return qs


def task_10_p43():
    # select * from emp where comm is null;
    qs = Emp.objects.filter(comm__isnull=True)
    return qs


def task_11_p44():
    # select coalesce(comm, 0) as comm_m from emp;
    qs = Emp.objects.annotate(comm_m=Coalesce('comm', Value(0))).values('comm_m')
    return qs


def task_11_1_p44():
    # select case when comm is null then 0 else comm end as comm_m from emp;
    qs = (Emp.objects
          .annotate(comm_m=Case(When(comm__isnull=True, then=Value(0)),
                                default=F('comm'),
                                output_field=IntegerField()))
          .values('comm_m'))
    return qs


def task_12_p45():
    # select ename, job from emp where deptno in (10, 20);
    qs = (Emp.objects
          .filter((Q(ename__contains='I') |
                   Q(ename__contains='ER')), deptno__in=(10, 20))
          .values('ename', 'job'))
    return qs


if __name__ == '__main__':
    print(task_1_p33())
    print(task_2_p34())
    print(task_2_1_p35())
    print(task_3_p35())
    print(task_4_p36())
    print(task_5_p37())
    print(task_6_p38())
    print(task_7_p39())
    print(task_8_p40())
    print(task_9_p42())
    print(task_10_p43())
    print(task_11_p44())
    print(task_11_1_p44())
    print(task_12_p45())

