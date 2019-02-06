# coding=utf-8
from django.db import models


class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=64)
    job = models.CharField(max_length=64)
    mgr = models.IntegerField(null=True)
    hiredate = models.DateField()
    sal = models.IntegerField()
    comm = models.IntegerField(null=True)
    deptno = models.IntegerField()

    class Meta:
        db_table = 'emp'
        managed = False

    def __str__(self):
        return self.ename

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.ename)


class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=64)
    loc = models.CharField(max_length=64)

    class Meta:
        db_table = 'dept'
        managed = False

    def __str__(self):
        return self.dname

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.dname)


class T1(models.Model):
    class Meta:
        db_table = 't1'
        managed = False


class T10(models.Model):
    class Meta:
        db_table = 't10'
        managed = False


class T100(models.Model):
    class Meta:
        db_table = 't100'
        managed = False

