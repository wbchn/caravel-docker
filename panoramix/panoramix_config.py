from dateutil import tz

PANORAMIX_WEBSERVER_PORT = 8080
PANORAMIX_WEBSERVER_TIMEOUT = 120

SQLALCHEMY_DATABASE_URI = 'sqlite:////panoramix/panoramix.db'

APP_NAME = "Druid Docker"

DRUID_TZ = tz.tzlocal()

BASE_DIR = '/panoramix'
UPLOAD_FOLDER = BASE_DIR + '/app/static/uploads/'
IMG_UPLOAD_FOLDER = BASE_DIR + '/app/static/uploads/'
IMG_UPLOAD_URL = '/static/uploads/'
