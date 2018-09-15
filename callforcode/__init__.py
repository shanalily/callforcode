from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt # need this to hash passwords later on

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

import callforcode.views