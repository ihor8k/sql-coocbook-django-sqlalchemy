# coding=utf-8
import os
import environ

from sqlalchemy import create_engine

os.environ['READ_DOT_ENV_FILE'] = 'true'

ROOT_DIR = environ.Path(__file__) - 2  # (alchemy/config.py - 2 = sqlcookbook-Djorm-Alchemy/)

# https://github.com/joke2k/django-environ#django-environ
env = environ.Env()

READ_DOT_ENV_FILE = env.bool('READ_DOT_ENV_FILE', default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR.path('.env')))

DEBUG = env.bool('DEBUG', default=True)

# https://docs.sqlalchemy.org/en/latest/core/tutorial.html#connecting
engine = create_engine(env.str('DATABASE_URL'), echo=DEBUG)
