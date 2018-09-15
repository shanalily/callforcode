from app import db

class User(db.Model):
	__tablename__ = "users"
	
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(200), unique=True, nullable=False)
	password = db.Column(db.String(200), nullable=False)

	cell_number = db.Column(db.String(10))

	# store location?

	def __init__(self, username, password):
		self.username = username
		self.password = generate_password_hash(password)

	def generate_password_hash(self, password):
		return bcrypt.generate_password_hash(password)