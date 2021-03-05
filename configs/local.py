import os
import datetime
from pathlib import Path
from configs.base import *
import environ

env = environ.Env()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# JWT
JWT_AUTH = {
    "JWT_EXPIRATION_DELTA": datetime.timedelta(hours=8),
    "JWT_AUTH_COOKIE": "token",
    "JWT_SECRET_KEY": env("JWT_KEY")
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        'request_id': {
            '()': 'log_request_id.filters.RequestIDFilter'
        }
    },
    "handlers": {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'filters': ['request_id'],
            'formatter': 'standard'
        },
    },
    "formatters": {
      "standard": {
        'format': "[%(asctime)s] %(levelname)s [%(request_id)s] [%(module)s.%(funcName)s:%(lineno)s] %(message)s",
        'datefmt': "%Y/%m/%d %H:%M:%S"
      },
    },
    "loggers": {
        "main": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "access":{
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "error": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
        'django.db.backends': {
            'handlers': ["console" ],
            'level': 'DEBUG',
            "propagate": True,
        },
    },
}