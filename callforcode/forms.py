from wtforms import Form, TextField, BooleanField, SelectField, validators
from callforcode.models import User, registered_user
from callforcode.states import states

class LoginForm(Form):
	username = TextField('Username', validators=[validators.required()])
	password = TextField('Password', validators=[validators.required()])

class RegisterForm(Form):
	username = TextField('Username', validators=[validators.required(), validators.Length(min=6)])
	password = TextField('Password', validators=[validators.required(), validators.Length(min=8)])

	first =  TextField('First Name', validators=[validators.required()])
	last =  TextField('Last Name', validators=[validators.required()])

	email = TextField('Email', validators=[validators.required()])
	cell_number = TextField('Cell Number', validators=[
		validators.required(), validators.Length(min=10, max=14), validators.Regexp("[0-9]+")]) # for now

	city = TextField('City', validators=[validators.required()])
	state = SelectField('State', choices=states, validators=[validators.required()])

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
		self.user = None

class AttributesForm(Form):
	# qualities that user has that they can use to help others
	# we will assign them to low, medium, or high risk zones for now
	car = BooleanField("I own a car")
	truck = BooleanField("I own a truck")
	boat = BooleanField("I own a boat")

	food = BooleanField("I can provide food")

	cpr = BooleanField("I am CPR trained")
	emt = BooleanField("I am EMT trained")
	contractor = BooleanField("I am a general contractor")

	labor = BooleanField("I can provide manual labor")
	distance = SelectField('Distance willing to travel',
		choices=[(10, '10 miles'), (50, '50 miles'), (100, '100 miles'), (2680, 'across the country')],
		validators=[validators.required()])