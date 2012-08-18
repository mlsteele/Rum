import os.path

PROJECT_MODULE = '.'.join(__name__.split('.')[:-2])

def path(location):
    return os.path.join(PROJECT_MODULE, location)

TEMPLATE_DIRS = (
    path('music/templates')
)

STATICFILES_DIRS = (
    path('music/static'),
)

TIME_ZONE = 'America/New_York'

LANGUAGE_CODE = 'en-us'

USE_I18N = False

USE_L10N = False

USE_TZ = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django_browserid.context_processors.browserid_form',
    'django.contrib.auth.context_processors.auth'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django_browserid.auth.BrowserIDBackend',
)

ROOT_URLCONF = 'web.urls'

WSGI_APPLICATION = 'web.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django_browserid',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',

    'web.main',
)

LOGIN_REDIRECT_URL = '/'

LOGIN_REDIRECT_URL_FAILURE = '/login-failed'

BROWSERID_CREATE_USER = True

def username(email):
    return email.replace('@', '_')

BROWSERID_USERNAME_ALGO = username
