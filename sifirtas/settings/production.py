import os
from .base import *
from .djoser_settings import *

DEBUG = True
ALLOWED_HOSTS = ['13.50.180.137', '127.0.0.1', 'localhost']
MEDIA_URL = 'media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

