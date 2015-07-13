import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'dk8ye!)$ecltu=xxy#m566rjel39xvf3-qdvpamfhv9^v^%%5n'

DEBUG = True

TEMPLATE_DEBUG = True

TTEMPLATE_DIRS = (
     os.path.join(BASE_DIR, 'templates/'),
)
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'polls',
    'smartmin',
    'guardian',
    'smartminmodels',
    'smartmin.users',
    'templates',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djangotest.urls'

WSGI_APPLICATION = 'djangotest.wsgi.application'

PERMISSIONS = {
  '*': ('create', 
        'read',  
        'update', 
        'delete', 
        'list'),  
}

GROUP_PERMISSIONS = {
    "Administrator": ('auth.user.*',),
}

ANONYMOUS_USER_ID = -1

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

SESSION_CACHE_ALIAS = "default"

LOGIN_URL = "/users/login/"

LOGOUT_URL = "/users/logout/"

LOGIN_REDIRECT_URL = "/home/"

LOGOUT_REDIRECT_URL = "/"

USER_ALLOW_EMAIL_RECOVERY= True

USER_FAILED_LOGIN_LIMIT = 3

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
