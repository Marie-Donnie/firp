"""
Django settings for firp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open('secret_key') as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']


# Application definition

INSTALLED_APPS = (
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fiches',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'stopforumspam',
    'captcha',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'stopforumspam.middleware.StopForumSpamMiddleware',
)

ROOT_URLCONF = 'firp.urls'

WSGI_APPLICATION = 'firp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
if DEBUG:
   STATIC_ROOT = os.path.join(BASE_DIR, '/static/')
else:
   STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/fiches/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'fiches/media')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
            'debug': True,
        },
    },
]

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

LOGIN_REDIRECT_URL = '/'

LOGIN_URL = "/accounts/login/"

AUTHENTICATION_BACKENDS = {
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
}

# AUTH_USER_MODEL = 'django.contrib.auth.models.User'

FORMAT_MODULE_PATH = 'firp.formats'

SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = "mandatory"

ACCOUNT_EMAIL_SUBJECT_PREFIX = "Fils de Garithos "

ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_USERNAME_MIN_LENGTH = 4

FILE_UPLOAD_MAX_MEMORY_SIZE = 1048576

EMAIL_HOST = 'localhost'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# You can control how often at most the update should be performed

SFS_CACHE_EXPIRE = 1  # day

# ...and how long back the log should remember the rejection of POSTS and IPs

SFS_LOG_EXPIRE = 1  # days

# To check ALL POST requests:

SFS_ALL_POST_REQUESTS = True


with open('recaptcha_sk') as f:
    recaptcha_sk = f.read().strip()

RECAPTCHA_PUBLIC_KEY = '6LegJysUAAAAAAPuJRH5DpjfqWAeg-8ksUuHX_uG'
RECAPTCHA_PRIVATE_KEY = recaptcha_sk

RECAPTCHA_USE_SSL = True

ACCOUNT_SIGNUP_FORM_CLASS = 'fiches.forms.AllauthSignupForm'
