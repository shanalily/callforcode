from callforcode import app
from flask import request, render_template

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	return "login"