import os
from unipath import Path
from decouple import config


#
# BASE DIRECTORY
#
BASE_DIR = Path(__file__).ancestor(3)

#
# SECRET KEY
#
SECRET_KEY = config("SECRET_KEY")

#
# APPLICATIONS
#
DJANGO_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
)

LOCAL_APPS = (
	'applications.devices',
    #
)

THIRD_PARTY_APPS = (
    "rest_framework",
    "rest_framework.authtoken",
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

#
# REST FRAMEWORK
#
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
}


#
# MIDDLEWARE
#
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

#
# ROOT URL CONFIGURATION
#
ROOT_URLCONF = "project.urls"

#
# TEMPLATES
#
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # adding template
            os.path.join(BASE_DIR, 'templates'),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

#
# WSGI APPLICATION
#
WSGI_APPLICATION = "project.wsgi.application"

#
# PASSWORD VALIDATION
#
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

#
# INTERNATIONALIZATION
#
LANGUAGE_CODE = "en-us"

TIME_ZONE = config("TIME_ZONE")

DATETIME_FORMAT = "%Y-%m-%d%H:%M:%S"

L10N = False

USE_TZ = False

#
# DEFAULT PRIMARY KEY FIEDL TYPE
#
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
