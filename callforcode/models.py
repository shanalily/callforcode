from callforcode import db
# from flask_bcrypt import generate_password_hash, check_password_hash
from werkzeug.security import generate_password_hash, check_password_hash
from callforcode import login_manager
from flask_login import UserMixin

class User(UserMixin, db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(200), unique=True, nullable=False)
	password = db.Column(db.String(200), nullable=False)

	first = db.Column(db.String(200), nullable=False)
	last = db.Column(db.String(200), nullable=False)

	email = db.Column(db.String(200), nullable=False)
	cell_number = db.Column(db.String(14), nullable=False)

	city = db.Column(db.String(200), nullable=False)
	state = db.Column(db.String(200), nullable=False)

	def __init__(self, username, password, first, last, email, cell_number, city, state):
		self.username = username
		self.password = generate_password_hash(password)
		self.first = first
		self.last = last
		self.email = email
		self.cell_number = cell_number
		self.city = city
		self.state = state

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return self.id

	def generate_password_hash(self, password):
		return generate_password_hash(password)

	def check_password_hash(self, password):
		return check_password_hash(self.password, password)

class Attributes(db.Model):
	__tablename__ = "attributes"

	id = db.Column(db.Integer, primary_key=True)

	car = db.Column(db.Boolean())
	truck = db.Column(db.Boolean())
	boat = db.Column(db.Boolean())

	food = db.Column(db.Boolean())

	cpr = db.Column(db.Boolean())
	emt = db.Column(db.Boolean())
	contractor = db.Column(db.Boolean())

	labor = db.Column(db.Boolean())

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

def registered_user(username):
	return User.query.filter_by(username=username).first()