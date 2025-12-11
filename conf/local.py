from .common import *

DEBUG = False
PUBLIC_REGISTER_ENABLED = False

# Secret key
SECRET_KEY = "__SECRET_KEY__"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "__DB_NAME__",
        "USER": "__DB_USER__",
        "PASSWORD": "__DB_PWD__",
        "HOST": "/var/run/postgresql",
        "PORT": "",
    }
}

# Redis & RabbitMQ
CELERY_BROKER_URL = "amqp://__RABBITMQ_USER__:__RABBITMQ_PWD__@localhost:5672/__RABBITMQ_USER__"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"

# Cache
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://localhost:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Media and Static
MEDIA_URL = "__PATH__/media/"
STATIC_URL = "__PATH__/static/"
MEDIA_ROOT = "__DATA_DIR__/media"
STATIC_ROOT = "__INSTALL_DIR__/taiga-back/static"

# Sites configuration
SITES = {
    "api": {
        "scheme": "https",
        "domain": "__DOMAIN__",
        "name": "api"
    },
    "front": {
        "scheme": "https",
        "domain": "__DOMAIN__",
        "name": "front"
    }
}

# Site URL configuration
SITE_URL = "https://__DOMAIN____PATH__"
TAIGA_URL = "https://__DOMAIN____PATH__"

# Email configuration (can be customized later)
DEFAULT_FROM_EMAIL = "__ADMIN__@__DOMAIN__"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Allowed hosts
ALLOWED_HOSTS = ["__DOMAIN__", "localhost", "127.0.0.1"]

# CORS
CORS_ALLOWED_ORIGINS = [
    "https://__DOMAIN__",
]
CORS_ALLOW_CREDENTIALS = True

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}

# Events
EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {
    "url": "amqp://__RABBITMQ_USER__:__RABBITMQ_PWD__@localhost:5672/__RABBITMQ_USER__"
}

# Celery
CELERY_ENABLED = True

# Security headers for reverse proxy
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
