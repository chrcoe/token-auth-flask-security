import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'development key'
    ADMINS = frozenset(['chrcoe@ieee.org', ])
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECURITY_TRACKABLE = True
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    # safe to turn this off because all requests are token-based generated
    # by the server
    WTF_CSRF_ENABLED = False
    SECURITY_REGISTERABLE = True
    SECURITY_TOKEN_MAX_AGE = 600  # 10 minutes, default: None


class DevelopmentConfig(Config):
    IS_LOCAL = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/dev.db'
    SERVER_NAME = 'testflask.local:5000'
    SECURITY_PASSWORD_SALT = 'something_super_secret_change_in_production'

    #  MAIL_SERVER = 'smtp.gmail.com'
    #  MAIL_PORT = 587
    #  MAIL_USE_TLS = True
    #  MAIL_USE_SSL = True
    #  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    #  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


class ProductionConfig(Config):
    IS_LOCAL = False
    DEBUG = False
    SECURITY_PASSWORD_SALT = 'something_super_secret_change_in_production'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
