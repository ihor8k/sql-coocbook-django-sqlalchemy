# coding=utf-8
from sqlalchemy import Table, Column, Integer, String, MetaData, Date

metadata = MetaData()

emp = Table(
    'emp', metadata,
    Column('empno', Integer, primary_key=True),
    Column('ename', String(length=64)),
    Column('job', String(length=64)),
    Column('mgr', Integer, nullable=True),
    Column('hiredate', Date),
    Column('sal', Integer),
    Column('comm', Integer, nullable=True),
    Column('deptno', Integer),
)

dept = Table(
    'dept', metadata,
    Column('deptno', Integer, primary_key=True),
    Column('dname', String(length=64)),
    Column('loc', String(length=64)),
)

t1 = Table(
    't1', metadata,
    Column('id', Integer, primary_key=True),
)

t10 = Table(
    't10', metadata,
    Column('id', Integer, primary_key=True),
)

t100 = Table(
    't100', metadata,
    Column('id', Integer, primary_key=True),
)
