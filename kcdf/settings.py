# Django settings for kcdf project.
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('John Wesonga', 'johnwesonga@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'kcdf_or_ke'             # Or path to database file if using sqlite3.
DATABASE_USER = 'kcdf_db'             # Not used with sqlite3.
DATABASE_PASSWORD = 'db01318kc76'         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/kcdfweb/webapps/kcdf.or.ke/media/'



# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''


# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'v_hwaxanqk*e!2=f8^(5@e=ge$!4@!fggr*c45vjc1+8@6e2m4'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.request",
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
     'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
     'kcdf.multihost.MultiHostMiddleware',

)

HOST_MIDDLEWARE_URLCONF_MAP=(
			    'kcdf.or.ke','kcdf.website.urls',
			    'ustawi.kcdf.or.ke','kcdf.ustawi.urls',
)

ROOT_URLCONF = 'kcdf.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/kcdfweb/webapps/kcdf.or.ke/templates/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'tinymce',
    'tagging',
    'sorl.thumbnail',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.flatpages',
    'django.contrib.sites',
    'kcdf.website',

    
)

#setting for django-tinymce
TINYMCE_JS_URL=MEDIA_URL + '/site_media/js/tiny_mce/tiny_mce.js'
TINYMCE_DEFAULT_CONFIG = {'theme': "advanced",
'plugins':"paste",
'theme_advanced_toolbar_location' : "top"
}
TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
    'kcdf.website.context_processors.header_context',
)
