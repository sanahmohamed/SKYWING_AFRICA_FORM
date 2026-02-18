import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-skywing-real-estate-secret-key-2024'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add WhiteNoise for static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'skywing_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'skywing_site.wsgi.application'

# ============================================================
# DATABASE — Microsoft SQL Server
# ============================================================
# STEP 1: pip install mssql-django pyodbc
# STEP 2: Install "ODBC Driver 17 for SQL Server" from Microsoft
# STEP 3: Create a database called 'skywing_db' in SQL Server
# STEP 4: Fill in your HOST, USER, PASSWORD below
# ============================================================
# DATABASES = {
#     'default': {
#         'ENGINE': 'mssql',
#         'NAME': 'skywing_db',            # ← Your SQL Server database name
#         'USER': 'sanah',                    # ← Your SQL Server username (or use Windows Auth below)
#         'PASSWORD': 'sanah@5355',   # ← Your SQL Server password
#         'HOST': 'localhost',             # ← SQL Server host (localhost or IP address)
#         'PORT': '1433',                  # ← Default SQL Server port
#         'OPTIONS': {
#             'driver': 'ODBC Driver 17 for SQL Server',
#             'extra_params': 'TrustServerCertificate=yes',
#         },
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / "db.sqlite3",
#     }
# }


if os.environ.get('DATABASE_URL'):
    # Production - PostgreSQL
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    # Local - SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ============================================================
# WINDOWS AUTHENTICATION (alternative — no username/password)
# Uncomment below and comment out the block above if you want
# to use your Windows login instead of SQL Server login:
# ============================================================
# DATABASES = {
#     'default': {
#         'ENGINE': 'mssql',
#         'NAME': 'skywing_db',
#         'HOST': 'localhost',
#         'PORT': '1433',
#         'OPTIONS': {
#             'driver': 'ODBC Driver 17 for SQL Server',
#             'trusted_connection': 'yes',
#             'extra_params': 'TrustServerCertificate=yes',
#         },
#     }
# }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dubai'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise configuration for production static files
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
