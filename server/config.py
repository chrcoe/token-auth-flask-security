import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'development key'
    ADMINS = frozenset(['chrcoe@ieee.org', ])
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECURITY_TRACKABLE = True
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'


class DevelopmentConfig(Config):
    IS_LOCAL = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/dev.db'
    SERVER_NAME = 'testflask.local:5000'
    SECURITY_PASSWORD_SALT = 'something_super_secret_change_in_production'


class ProductionConfig(Config):
    IS_LOCAL = False
    DEBUG = False
    SECURITY_PASSWORD_SALT = 'something_super_secret_change_in_production'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
