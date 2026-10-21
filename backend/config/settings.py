"""
Django settings for Travel First Holidays project.
Configured for production with environment variable support,
PostgreSQL database, and local SQLite fallback.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    # Checks both backend/.env and project root .env
    load_dotenv(BASE_DIR / '.env')
    load_dotenv(BASE_DIR.parent / '.env')
except ImportError:
    pass

# ==============================================================================
# CORE SECURITY SETTINGS
# ==============================================================================

# DEBUG mode: Defaults to True for local development if no .env exists;
# set to DEBUG=False in production .env.
if 'DEBUG' in os.environ:
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ('true', '1', 'yes')
else:
    DEBUG = True

# SECRET_KEY: Must be provided via environment in production (DEBUG=False).
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    if DEBUG:
        SECRET_KEY = 'django-insecure-travelfirst-dev-fallback-key-2026'
    else:
        raise ValueError(
            "CRITICAL: The SECRET_KEY environment variable is missing. "
            "Set SECRET_KEY in your production .env file."
        )

# Allowed Hosts
_env_allowed_hosts = os.environ.get('ALLOWED_HOSTS', '')
if _env_allowed_hosts:
    ALLOWED_HOSTS = [h.strip() for h in _env_allowed_hosts.split(',') if h.strip()]
else:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', '[::1]']

# ==============================================================================
# APPLICATION DEFINITION
# ==============================================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party packages
    'corsheaders',
    'rest_framework',

    # Local apps
    'tours',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # Handles CORS headers early
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.parent],
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

WSGI_APPLICATION = 'config.wsgi.application'

# ==============================================================================
# DATABASE CONFIGURATION
# ==============================================================================
# Supports PostgreSQL in production and SQLite for local development

DB_ENGINE = os.environ.get('DB_ENGINE', 'django.db.backends.sqlite3')

if DB_ENGINE == 'django.db.backends.postgresql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME', 'girgujarat_db'),
            'USER': os.environ.get('DB_USER', 'girgujarat_user'),
            'PASSWORD': os.environ.get('DB_PASSWORD', ''),
            'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
            'PORT': os.environ.get('DB_PORT', '5432'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ==============================================================================
# PASSWORD VALIDATION
# ==============================================================================

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

# ==============================================================================
# DJANGO REST FRAMEWORK SETTINGS
# ==============================================================================

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
}

# ==============================================================================
# CORS & CSRF CONFIGURATION
# ==============================================================================

_env_cors_origins = os.environ.get('CORS_ALLOWED_ORIGINS', '')
if _env_cors_origins:
    CORS_ALLOWED_ORIGINS = [o.strip() for o in _env_cors_origins.split(',') if o.strip()]
else:
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5500",
        "http://127.0.0.1:5500",
    ]

CORS_ALLOW_CREDENTIALS = True

_env_csrf_origins = os.environ.get('CSRF_TRUSTED_ORIGINS', '')
if _env_csrf_origins:
    CSRF_TRUSTED_ORIGINS = [o.strip() for o in _env_csrf_origins.split(',') if o.strip()]
else:
    CSRF_TRUSTED_ORIGINS = list(CORS_ALLOWED_ORIGINS)

# Ensure CSRF cookie is accessible to JavaScript for Fetch requests
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SAMESITE = 'Lax'

# ==============================================================================
# INTERNATIONALIZATION
# ==============================================================================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# ==============================================================================
# STATIC & MEDIA FILES
# ==============================================================================

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR.parent / 'css',
    BASE_DIR.parent / 'js',
    BASE_DIR.parent / 'assets',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
