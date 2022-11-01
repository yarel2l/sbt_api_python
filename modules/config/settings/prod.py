from .base import *
from decouple import config

DEBUG = False

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True

EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"

FILE_UPLOAD_PERMISSIONS = 0o644

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("POSTGRES_HOST"),
        "PORT": config("POSTGRES_PORT"),
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


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

ALLOWED_HOSTS = ["*", "34.230.40.43", "sbt.codevbros.com", "codevbros.com"]

CORS_ALLOWED_ORIGINS = [
    "https://scorbot.com",
    "https://dev.scorbot.com",
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")