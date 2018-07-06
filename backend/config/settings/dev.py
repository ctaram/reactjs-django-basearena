from .base import *  
from .base import env


# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('TODO_DJANGO_DEBUG', default=True)
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env('TODO_DJANGO_SECRET_KEY', default='^t@%0_4@p57)10v=w^+b8yw9u)q+jrs$v=^hxtd6-(b@e55l(*')
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS += [
    '127.0.0.1',
    '0.0.0.0',
    'localhost',
]

# Add OpenAPI Docs
INSTALLED_APPS.append('drf_yasg') 