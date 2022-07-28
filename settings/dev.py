from settings.base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": dj_database_url.config(conn_max_age=600, ssl_require=False),
}

EMAIL_SUBJECT_PREFIX = u"[\u2708\u2708\u2708DEVELOPMENT\u2708\u2708\u2708] "

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
