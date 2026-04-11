from datetime import timedelta
import os

# add local settings in this file 

# BASE_DIR = Path(_file_).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'change-me-locally')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'


# sql lite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# mssql
DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "NAME": "starter_code",
        "USER": "sa",
        "PASSWORD": "matthewpass26>0",
        "HOST": "127.0.0.1",
        "PORT": "1433",
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server",},
    },
}

# DATABASES = {
#     "default": {
#         "ENGINE": "mssql",
#         "NAME": "nema_test",
#         "USER": "sa",
#         "PASSWORD": "yoya@123@#",
#         "HOST": "localhost",   # match Azure Data Studio exactly
#         "PORT": "1433",
#         "OPTIONS": {
#             "driver": "ODBC Driver 18 for SQL Server",
#             "Encrypt": False,                 # <-- BOOLEAN
#             "TrustServerCertificate": False,  # <-- BOOLEAN
#         },
#     }
# }

# email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'relay.umcs.go.ug'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'ELMIS@nema.go.ug'
EMAIL_HOST_PASSWORD = 'YL1wNvDkLWxbmJhBHZZstAUH'
DEFAULT_FROM_EMAIL = 'ELMIS@nema.go.ug'

# PRN_API = 'http://iras.go.ug:8088/service/prn'
PRN_API = 'http://154.72.195.126:8088/service/prn'
NEMA_PRN_TAX_HEAD = '052-005-004'


CORS_ALLOW_ALL_ORIGINS = True

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=3600),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1)
}

SERVICE_URL = "https://service.iras.go.ug/"

IRAS_URL = "http://iras.go.ug/"

PASSWORD_RESET_LINK = 'http://127.0.0.1:8000/'

EXTERNAL_USER_EMAIL = 'external.user@nema.com'
EXTERNAL_USER_FIRST_NAME = 'Unauthenticated'
EXTERNAL_USER_LAST_NAME = 'User'

FRONTEND_URL = 'http://localhost:3000/'

UNAUTHENTICATED_API_TOKEN = ['XFGGHDTTYTYYGHERTYG',]

#Log out user after some minutes of inactivity or when browser closes
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 100 * 60
SESSION_SAVE_EVERY_REQUEST = True

ALLOWED_HOSTS = ['*', 'e281-41-75-180-51.eu.ngrok.io']

CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Redis as broker

CELERY_TASK_ALWAYS_EAGER = True  #WARNING: Run tasks synchronously for testing and development
CELERY_TASK_EAGER_PROPAGATES = True  #WARNING: Run tasks synchronously for testing and development

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#         },
#     },
#     "loggers": {
#         "django.db.backends": {
#             "handlers": ["console"],
#             "level": "DEBUG",  # change to INFO to reduce noise
#         },
#     },
# }