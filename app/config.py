import os
BASE_DIR = os.getcwd()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False

# Don't use DEBUG=True in production environment
DEBUG = True

# CAT CWS OAuth using QA configs
OAUTH_QA = False

# Flask JWT Extended
JWT_SECRET_KEY = Config.SECRET_KEY
JWT_TOKEN_LOCATION = ['cookies']
JWT_ACCESS_COOKIE_PATH = '/'
JWT_COOKIE_CSRF_PROTECT = True
# Only allow https
JWT_COOKIE_SECURE = False
JWT_ERROR_MESSAGE_KEY = "message"
JWT_ACCESS_TOKEN_EXPIRES = False

# Flask SQLAlchemy
SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URL", "sqlite:///" + os.path.join(BASE_DIR, 'db.sqlite')) # Place db.sqlite at root folder
SQLALCHEMY_TRACK_MODIFICATIONS = False

key = Config.SECRET_KEY