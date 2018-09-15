from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = os.environ['CFC_SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://shanalily:frogandtoad@localhost/callforcode'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

import callforcode.views

db.create_all()