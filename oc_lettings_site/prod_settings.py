from .settings import *
import dj_database_url

DATABASE_URL = os.environ.get('DATABASE_URL')
db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)

SECRET_KEY = os.environ.get('SECRET_KEY', default='foo')

DEBUG = int(os.environ.get('DEBUG', default=0))

#DEBUG = False
#TEMPLATE_DEBUG = False

#ALLOWED_HOSTS = ['p13-open-class-room.herokuapp.com']
ALLOWED_HOSTS = ['localhost', '127.0.0.1','p13-open-class-room.herokuapp.com']

#DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)