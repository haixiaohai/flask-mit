#! python3
# -*- encoding:utf-8 -*-

'Maipu Inspection Tools'
__version__ = '0.1'
__author__ = '006007'


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_script import Manager
from flask_bootstrap import Bootstrap
#from wx import Frame,App
#from wx.adv import TaskBarIcon
from flask_nav import Nav
from flask_nav.elements import *


#app init
webapp = Flask(__name__)
webapp.config.from_object('config')


#database init
db = SQLAlchemy(webapp)
migrate = Migrate(webapp,db)

#loginmanager init
login = LoginManager(webapp)
login.login_view = 'sign_in'

#script init
manager = Manager(webapp)

#bootstrap init
bootstrap = Bootstrap(webapp)


#nav init

from app import routes