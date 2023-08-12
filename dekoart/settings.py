from pathlib import Path
from datetime import timedelta
from django.utils.translation import gettext_lazy as _
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pui&ui7*lg3lwtm79$b^ws%-m_o6z^bq5i(6_yw8ar+tn#u#l%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'authentication.User'

# Application definition

INSTALLED_APPS = [
    'modeltranslation',  # translation

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # packeges
    'rest_framework',
    'corsheaders',
    'django_filters',
    'drf_yasg',
    'ckeditor',
    'ckeditor_uploader',

    'parler',

    # apps
    'apps.authentication',
    'apps.core',
    'apps.dictionary',
    'apps.products',

]

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ASGI_APPLICATION = 'edu_server.routing.application'

ROOT_URLCONF = 'dekoart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dekoart.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

CORS_ORIGIN_ALLOW_ALL = True

# CSRF_TRUSTED_ORIGINS = ["https://otabekismailov.jprq.live/", "http://localhost:3000"]

CORS_ALLOW_METHODS = [
    '*'
]

CORS_ALLOW_HEADERS = [
    '*'
]
CORS_ALLOW_CREDENTIALS = True

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Translation

# Languages supported by translation
MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'

LANGUAGES = (
    ('uz', _('Uzbek')),
    ('ru', _('Russian')),
)

MODELTRANSLATION_LANGUAGE = ('ru', 'uz')

MODELTRANSLATION_FALLBACK_LANGUAGES = ('uz', 'ru')

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

MODELTRANSLATION_TRANSLATION_FILES = (
    'apps.core.translation',
    'apps.dictionary.translation',
    'apps.products.translation',
)

TRANSLATABLE_MODEL_MODULES = [
    'apps.core.models',
    'apps.dictionary.models',
    'apps.products.models',
]

PARLER_LANGUAGES = {
    None: (
        {'code': 'uz', },  # Uzbek
        {'code': 'ru', },  # Russian
    ),
    'default': {
        'fallbacks': ['uz'],
        'hide_untranslated': False,
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

CKEDITOR_UPLOAD_PATH = "uploads/"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DATE_INPUT_FORMATS': ["%d.%m.%Y", ],
    'DATETIME_FORMAT': "%d.%m.%Y",
    'PAGE_SIZE': 10
}
# swagger ->
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

USE_X_FORWARDED_HOST = True

DATETIME_FORMAT = ("%d.%m.%Y",)

SILENCED_SYSTEM_CHECKS = ["rest_framework.W001"]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=2),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=30),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    'AUTH_COOKIE': 'access_token',  # Cookie name. Enables cookies if value is set.
    # Cookie name. Enables cookies if value is set.
    'AUTH_COOKIE_DOMAIN': None,  # A string like "example.com", or None for standard domain cookie.
    'AUTH_COOKIE_SECURE': False,  # Whether the auth cookies should be secure (https:// only).
    'AUTH_COOKIE_HTTP_ONLY': True,  # Http only cookie flag.It's not fetch by javascript.
    'AUTH_COOKIE_PATH': '/',  # The path of the auth cookie.
    'AUTH_COOKIE_SAMESITE': 'Lax',
}

# SECURE_BROWSER_XSS_FILTER = True
# X_FRAME_OPTIONS = 'DENY'

# SECURE_SSL_REDIRECT = False
# SESSION_COOKIE_SECURE = False
# CSRF_COOKIE_SECURE = False

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
