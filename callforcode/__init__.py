from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)
app.secret_key = os.environ['CFC_SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://shanalily:frogandtoad@localhost/callforcode'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db = SQLAlchemy(app)

import callforcode.views

db.create_all()