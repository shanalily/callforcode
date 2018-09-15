from callforcode import app, db
from flask import request, render_template, redirect, url_for, flash
from callforcode.models import User, registered_user
from callforcode.forms import LoginForm, RegisterForm, AttributesForm
from flask_login import login_user, logout_user, login_required

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	# if current_user.is_authenticated:
	# 	return redirect(url_for('index'))
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		username = request.form['username']
		password = request.form['password']
		user = registered_user(username, password)
		print("user", user)
		if user is None:
			flash('Invalid username or password')
			return redirect(url_for('login'))
		print(user)
		login_user(user)
		flash('Logged in successfully')
		return redirect(url_for('index'))
	return render_template('login.html', form=form)

@app.route('/create-account', methods=['GET', 'POST'])
def create_account():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		username = request.form['username']
		password = request.form['password']
		first = request.form['first']
		last = request.form['last']
		email = request.form['email']
		cell_number = request.form['cell_number']
		city = request.form['city']
		state = request.form['state']
		user = User(username, password, first, last, email, cell_number, city, state)
		db.session.add(user)
		db.session.commit()
		login_user(user)
		flash('Successfully created account')
		return redirect(url_for('index'))
	return render_template('create_account.html', form=form)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/settings', methods=['GET', 'POST'])
# @login_required
def settings():
	form = AttributesForm(request.form)
	if request.method == 'POST' and form.validate():
		req = request.form.getlist('option')
		print("request", req)
	return render_template('settings.html', form=form)