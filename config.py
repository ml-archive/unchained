import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    THREADS_PER_PAGE = 2
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "$g8$sd*58x*g&xx0b3ma!-iob&_kpn&jeju1_*r)i^a@3+z8)j"
    SECRET_KEY = "4g8$77sda242sda0b3ma!-iob&_kpn&jeju1_*t)i^a@3+z3)j"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'development.db')
    DATABASE_CONNECT_OPTIONS = {}


class Testing(Config):
    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    HASH_ROUNDS = 1
class Production(Config):
    DEBUG = False




config = {
    'development': Development,
    'testing': Testing,
    'production': Production,
    'default': Development
}
