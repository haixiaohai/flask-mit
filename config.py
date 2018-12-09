import os

#
DEBUG = True

#
CSRF_ENABLED = True    #cross-site request forgery
SECRET_KEY = 'you-will-never-guess'

#database setup
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False