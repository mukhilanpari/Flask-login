"""Flask Login Example and instagram fallowing find"""

from flask import Flask, url_for, render_template, flash, request, redirect, session,logging,request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User(db.Model):
	""" Create user table"""
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	password = db.Column(db.String(80))

	def __init__(self, username, password):
		self.username = username
		self.password = password
        
class Profile(db.Model):
	""" Create profile table"""
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	dob = db.Column(db.String(80))
	email = db.Column(db.String(80))
	ssn = db.Column(db.String(80))

	def __init__(self, name, dob, email, ssn):
		self.name = name
		self.dob = dob
		self.email = email
		self.ssn = ssn


@app.route('/', methods=['GET', 'POST'])
def home():
	""" Session control"""
	if not session.get('logged_in'):
		return render_template('index.html')
	else:
		if request.method == 'POST':

			return render_template('index.html') 
		return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	"""Login Form"""
	if request.method == 'GET':
		return render_template('login.html')
	else:
		name = request.form['username']
		passw = request.form['password']
		try:
			data = User.query.filter_by(username=name, password=passw).first()
			if data is not None:
				session['logged_in'] = True
				return redirect(url_for('home'))
			else:
				return 'Incorrect Login'
		except:
			return "Incorrect Login"

@app.route('/register/', methods=['GET', 'POST'])
def register():
	"""Register Form"""
	if request.method == 'POST':
		new_user = User(username=request.form['username'], password=request.form['password'])
		db.session.add(new_user)
		db.session.commit()
		return render_template('login.html')
	return render_template('register.html')
    
@app.route('/profile/', methods=['GET', 'POST'])
def profile():
	"""Register Form"""
	if request.method == 'POST':
		new_profile = Profile(name=request.form['name'], dob=request.form['dob'], email=request.form['email'], ssn=request.form['ssn'])
		db.session.add(new_profile)
		db.session.commit()
		return render_template('index.html')
	return render_template('index.html')


@app.route("/logout")
def logout():
	"""Logout Form"""
	session['logged_in'] = False
	return redirect(url_for('home'))


if __name__ == '__main__':
	app.debug = True
	db.create_all()
	app.secret_key = "123"
	app.run(host='0.0.0.0')
	
