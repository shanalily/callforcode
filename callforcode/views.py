from callforcode import app, db
from flask import request, render_template, redirect, url_for, flash
from callforcode.models import User, Attributes, registered_user, load_user
from callforcode.forms import LoginForm, RegisterForm, AttributesForm
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	# current issue: user is authenticated even when they shouldn't be
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		username = request.form['username']
		password = request.form['password']
		user = registered_user(username)
		if user is None or not user.check_password_hash(password):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user, True)
		flash('Logged in successfully')
		return redirect(url_for('index'))
	return render_template('login.html', form=form)

@app.route('/create-account', methods=['GET', 'POST'])
def create_account():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		username = request.form['username']
		if not registered_user(username):
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
			return redirect(url_for('settings'))
		else:
			flash("Username already taken")
	return render_template('create_account.html', form=form)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
	form = AttributesForm(request.form)
	car = False
	truck = False
	boat = False
	food = False
	cpr = False
	emt = False
	contractor = False
	labor = False
	if request.method == 'POST': # should have form.validate() but I'm not sure why validation is failing
		userid = current_user.get_id()
		if request.form.get('1'):
			car = True
		if request.form.get('2'):
			truck = True
		if request.form.get('3'):
			boat = True
		if request.form.get('4'):
			food = True
		if request.form.get('5'):
			cpr = True
		if request.form.get('6'):
			emt = True
		if request.form.get('7'):
			contractor = True
		if request.form.get('8'):
			labor = True
		distance = int(request.form['distance'])
		attributes = Attributes.query.filter_by(userid=userid).first()
		if attributes is None:
			attributes = Attributes(userid, car, truck, boat, food, cpr, emt, contractor, labor, distance)
			db.session.add(attributes)
			db.session.commit()
		else:
			attributes.update(car, truck, boat, food, cpr, emt, contractor, labor, distance)
		return redirect(url_for('index'))
	return render_template('settings.html', form=form)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	return render_template('contact.html')

@app.route('/needed')
def needed():
	return render_template('needed.html')

@app.route('/watch')
def watch():
	return render_template('disaster_watch.html')