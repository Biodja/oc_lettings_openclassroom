from .settings import *
import dj_database_url

DATABASES['default'] = dj_database_url.config()


DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['p13-open-class-room.herokuapp.com' , '127.0.0.1']

