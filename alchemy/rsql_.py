# coding=utf-8
from sqlalchemy import select
from alchemy.config import engine
from alchemy.core import db

with engine.connect() as conn:
    emp = select([db.emp])
    results = conn.execute(emp)
    for r in results:
        print(r)
