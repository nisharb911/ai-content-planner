# backend/settings.py

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True
ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'backend.urls'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': 'aws-1-ap-southeast-1.pooler.supabase.com',
#         'PORT': '5432',  # Session Pooler port
#         'NAME': 'postgres',
#         'USER': 'postgres.abgwckaegluhqqvtafgo',
#         'PASSWORD': 'Nisharb911@26',
#         'OPTIONS': {
#             'sslmode': 'require',
#         }
#     }
# }
# for live deploye project
import dj_database_url

DATABASES = {
   'default': dj_database_url.config(
       default=os.environ.get("DATABASE_URL"),
       conn_max_age=600,
       ssl_require=True
   )
}


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',   # ← ADD THIS
    'planner',          # your app
    
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}

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

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',    # REQUIRED
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # REQUIRED
    'django.contrib.messages.middleware.MessageMiddleware',    # REQUIRED
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

SECRET_KEY = 'django-insecure-3x!u1$8@%k9d1b&cz2#d7l5u@o4l9h1r!g4f8u^7$!j8v2r@p'
