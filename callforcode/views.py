from callforcode import app
from flask import request, render_template

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
	return render_template('login.html')

@app.route('/create-account', methods=['GET'])
def create_account():
	return render_template('login.html')