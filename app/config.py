import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Forms and auth secret key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    EXPIRATION_INCREASE_HOURS = int(os.environ.get('EXPIRATION_INCREASE_HOURS') or 6)
