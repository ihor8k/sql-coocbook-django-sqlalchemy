# codding=utf-8
import os
import sys
import environ

from django.conf import settings

os.environ['READ_DOT_ENV_FILE'] = 'true'

ROOT_DIR = environ.Path(__file__) - 2  # (django_orm/config.py - 2 = sqlcookbook-Djorm-Alchemy/)

# https://github.com/joke2k/django-environ#django-environ
env = environ.Env()

READ_DOT_ENV_FILE = env.bool('READ_DOT_ENV_FILE', default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR.path('.env')))

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DEBUG', default=True)

# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': env.db('DATABASE_URL')
}

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = [
    'django_orm.core'
]

# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = '%$R##ˆSewytsg2#Y@yt'

# https://docs.djangoproject.com/en/2.1/topics/settings/#using-settings-without-setting-django-settings-module
settings.configure(
    SECRET_KEY=SECRET_KEY,
    DATABASES=DATABASES,
    DEBUG=DEBUG,
    INSTALLED_APPS=INSTALLED_APPS
)


if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
