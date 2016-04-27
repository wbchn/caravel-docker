
from dateutil import tz

#---------------------------------------------------------
# Caravel specifix config
#---------------------------------------------------------
ROW_LIMIT = 5000
WEBSERVER_THREADS = 8

CARAVEL_WEBSERVER_PORT = 8088
caravel_WEBSERVER_TIMEOUT = 300

APP_NAME = "Druid Docker"

DRUID_TZ = tz.tzlocal()
#---------------------------------------------------------

#---------------------------------------------------------
# Flask App Builder configuration
#---------------------------------------------------------
# Your App secret key
SECRET_KEY = '\2\1thisismyscretkey\1\2\e\y\y\h'

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# caravel metadata (slices, connections, tables, dashboards, .).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
SQLALCHEMY_DATABASE_URI = 'sqlite:////caravel/caravel.db'

# Flask-WTF flag for CSRF
CSRF_ENABLED = True



