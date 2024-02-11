import os
from .base import *
from .djoser_settings import *
DEBUG = False
ALLOWED_HOSTS = ['13.50.180.137']
MEDIA_URL = 'media/'
STATIC_URL = 'static/'
STATIC_ROOT = 'staticfiles/'
STATICFILES_DIRS = [
    BASE_DIR / 'static/' # Here
    ]