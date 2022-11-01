from .base import *

DEBUG = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

AUTH_PASSWORD_VALIDATORS = []

# # Media files
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = "/media/"

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'scorbot': {
        'ENGINE': 'mssql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            # "setdecoding": [
            #     {"sqltype": pyodbc.SQL_CHAR, "encoding": 'utf-8'},
            #     {"sqltype": pyodbc.SQL_WCHAR, "encoding": 'utf-8'}],
            "setencoding": [
                {"encoding": "utf-8"}],
            },
    }
}
DATABASE_CONNECTION_POOLING = False
