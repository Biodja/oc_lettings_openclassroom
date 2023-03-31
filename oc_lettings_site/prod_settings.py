from .settings import *
import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)



DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['p13-open-class-room.herokuapp.com']

#DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)