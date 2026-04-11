from datetime import timedelta
import os

from pension.settings import BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'change-me-locally')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# mssql (example)
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': os.environ.get('DB_NAME', 'pension_db'),
        'USER': os.environ.get('DB_USER', 'sa'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DB_PORT', '1433'),
        'OPTIONS': {
            'driver': os.environ.get('ODBC_DRIVER', 'ODBC Driver 17 for SQL Server'),
            'extra_params': 'TrustServerCertificate=yes',
        },
    },
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=int(os.environ.get('ACCESS_TOKEN_MINUTES', 800000))),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=int(os.environ.get('REFRESH_TOKEN_DAYS', 365))),
    'UPDATE_LAST_LOGIN': True,
}


CORS_ALLOW_ALL_ORIGINS = True

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['http://localhost:3000']
SERVICE_URL = os.environ.get('SERVICE_URL', 'https://service.test.iras.go.ug')

FRONTEND_URL = os.environ.get('FRONTEND_URL', 'https://v3.iras.go.ug/')

PASSWORD_RESET_LINK = None

IRAS_URL = ''


AUTHENTICATION_BACKENDS = [
    'pension_auth.auth_backends.EmailOrPhoneBackend',
    'pension_auth.auth_backends.ExpiryCheckedModelBackend',
]

EXTERNAL_USER_EMAIL = 'external.user@pension.go.ug'
EXTERNAL_USER_FIRST_NAME = 'Unauthenticated'
EXTERNAL_USER_LAST_NAME = 'User'


SERVICE_URL = "https://service.test.iras.go.ug"

URA_API = ""
