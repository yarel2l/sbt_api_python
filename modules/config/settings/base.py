import os
from decouple import config

from django.contrib import messages

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = config('SECRET_KEY')

DEBUG = True
SITE_ID = 1
SITE_NAME = 'SCORBOT API'


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'rest_framework',
    'rest_framework.authtoken',
    'drf_spectacular',
    'corsheaders',

    'anymail',
    'allauth',
    'allauth.account',
    'django_filters',
    'django_select2',
    'django_tables2',
    'widget_tweaks',
    'phonenumber_field',
    'django_gravatar',
    'django_short_url',
    'sekizai',

    'iam',
    'v1',
    'core',
    'states',
    'users',
    'organizations',
    'tournaments',
    'divisions',
    'pools',
    'teams',
    'facilities',
    'games',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'iam.middleware.timezone.TimezoneMiddleware',
    'iam.middleware.custom_locale.CustomLocaleMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.static',
                'sekizai.context_processors.sekizai',
                'core.context_processors.global_params',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Internationalization
gettext = lambda s: s
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ("en", "English"),
    ("es", "Español"),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SPECTACULAR_SETTINGS = {
    'TITLE': SITE_NAME,
    # 'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'CAMELIZE_NAMES': False,
    'COMPONENT_SPLIT_REQUEST': True,
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'filter': True,
        'displayRequestDuration': True,
        'syntaxHighlight.activate': True,
        'syntaxHighlight.theme': 'monokai',
    },
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "v1.exception_handler.custom_exception_handler",
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework_datatables.renderers.DatatablesRenderer",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework_datatables.filters.DatatablesFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework_datatables.pagination.DatatablesPageNumberPagination',
    'PAGE_SIZE': 15,
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
}

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "mail_admins": {"level": "ERROR", "class": "django.utils.log.AdminEmailHandler", "formatter": "verbose"},
#         "console": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "verbose"},
#         "logfile": {
#             "level": "INFO",
#             "class": "logging.handlers.TimedRotatingFileHandler",
#             "filename": os.path.join(BASE_DIR, "logs/system.log"),
#             "when": "midnight",
#             "interval": 1,
#             "backupCount": 100,
#             "formatter": "verbose",
#         },
#     },
#     "formatters": {
#         "verbose": {
#             "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             "datefmt": "%d/%b/%Y %H:%M:%S",
#         }
#     },
#     "loggers": {
#         "": {
#             "handlers": ["console", "logfile"],
#             "level": "INFO",
#             "propagate": True
#         },
#         "django": {
#             'handlers': ['console'],
#             'level': 'WARNING',
#         },
#     },
# }


# AUTH
AUTH_USER_MODEL = "iam.User"
LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = "/"

ACCOUNT_ADAPTER = "iam.account_adapter.CustomAllauthAdapter"
# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_MAX_EMAIL_ADDRESSES = 1

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 5
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_CONFIRMATION_HMAC = False
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 5
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_LOGOUT_ON_GET = True

ACCOUNT_USERNAME_BLACKLIST = ["admin", "support", "info"]

ACCOUNT_FORMS = {
    "login": "iam.forms.MyCustomLoginForm",
    "signup": "iam.forms.MyCustomSignupForm",
    "reset_password": "iam.forms.MyCustomResetPasswordForm"
}

REDIS_HOST = config("REDIS_HOST", "127.0.0.1")
REDIS_PORT = config("REDIS_PORT", 6379)
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"{REDIS_URL}/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PARSER_CLASS": "redis.connection.HiredisParser",
        },
    },
    'select2': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"{REDIS_URL}/3",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Set the cache backend to select2
SELECT2_CACHE_BACKEND = 'select2'
SELECT2_CSS = ''
SELECT2_JS = ''

# messages
MESSAGE_TAGS = {
    messages.DEBUG: "bg-secondary secondary",
    messages.INFO: "bg-info border-info",
    messages.SUCCESS: "bg-success border-success",
    messages.WARNING: "bg-warning border-warning",
    messages.ERROR: "bg-danger border-danger",
}


GRAVATAR_DEFAULT_RATING = "g"   # One of the following: ‘g’, ‘pg’, ‘r’, ‘x’. Defaults to ‘g’
GRAVATAR_DEFAULT_IMAGE = "monsterid"  # ‘mm’, ‘identicon’, ‘monsterid’, ‘wavatar’, ‘retro’


# DJANGO_TABLES2
DJANGO_TABLES2_TEMPLATE = "table2_template.html"


# Anymail config for SendGrid service
ANYMAIL = {
    "SENDGRID_API_KEY": config("SENDGRID_API_KEY", default=None),
    "SENDGRID_MERGE_FIELD_FORMAT": "-{}-",
}
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[SBT]"

# Phonenumbers settings
PHONENUMBER_DB_FORMAT = "E164"
PHONENUMBER_DEFAULT_FORMAT = "E164"
PHONENUMBER_DEFAULT_REGION = "US"