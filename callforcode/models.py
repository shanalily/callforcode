from callforcode import db
from flask_bcrypt import generate_password_hash
from callforcode import login_manager

class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(200), unique=True, nullable=False)
	password = db.Column(db.String(200), nullable=False)

	cell_number = db.Column(db.String(14), nullable=False)

	city = db.Column(db.String(200), nullable=False)
	state = db.Column(db.String(200), nullable=False)

	def __init__(self, username, password, cell_number, city, state):
		self.username = username
		self.password = generate_password_hash(password)
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
		return bcrypt.generate_password_hash(password)

	def check_password_hash(self, password):
		return bcrypt.check_password_hash(password)

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

def registered_user(username, password):
	return User.query.filter_by(username=username, password=str(generate_password_hash(password))).first()