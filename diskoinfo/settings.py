"""
Django settings for diskoinfo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from django.conf.global_settings import STATICFILES_FINDERS, TEMPLATE_CONTEXT_PROCESSORS
from django.core.urlresolvers import reverse_lazy
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u3=1)l^99ugzlyav!zbfb6-7mdad8t#_$%$x9-88-qhjb+ytww'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    'tinymce',
    'compressor',
    'bootstrapform',
    'django.contrib.admin',

    'diskoinfo',
    'zapisnik',
    'termini',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'diskoinfo.urls'

WSGI_APPLICATION = 'diskoinfo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'sqlite.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'hr-hr'
TIME_ZONE = 'Europe/Zagreb'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

# Every RequestContext will contain a variable request, required for admin dashboard
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)


GRAPPELLI_ADMIN_TITLE = '<a href="/">Disko Info</a>'
GRAPPELLI_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'

# Main FileBrowser Directory 'uploads/'. Leave empty in order to browse all from MEDIA_ROOT
FILEBROWSER_DIRECTORY = ''
FILEBROWSER_DEFAULT_SORTING_BY = 'filename_lower'

FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail (60px)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small (140px)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (300px)', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (460px)', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large (680px)', 'width': 680, 'height': '', 'opts': ''},
}
# Versions available within the Admin-Interface.
FILEBROWSER_ADMIN_VERSIONS = ['thumbnail', 'small', 'medium', 'big', 'large']
# Which Version should be used as Admin-thumbnail.
FILEBROWSER_ADMIN_THUMBNAIL = 'admin_thumbnail'

FILEBROWSER_SELECT_FORMATS = {
    'File': ['Folder','Document',],
    'Image': ['Folder','Image',],
    'Media': ['Video','Sound'],
    'Document': ['Document'],
    # for TinyMCE we can also define lower-case items
    'image': ['Image'],
    'file': ['Folder','Image','Document',],
}

# tinymce settings, add/remove buttons and so on
TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_resizing' : True,
    'plugins' : 'table,contextmenu,paste,autoresize,media,lists,style',
    # 'height' : 600,
    # 'width' : 800,
    'theme_advanced_buttons1': "formatselect,style,bold,italic,underline,separator,bullist,separator,outdent,indent,separator,undo,redo",
    'theme_advanced_buttons2': "cleanup,code,separator,lists,pasteword,table,contextmenu,media,style,image,link",
    # 'theme_advanced_buttons3': "",
}

LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')
LOGIN_REDIRECT_URL = '/'
