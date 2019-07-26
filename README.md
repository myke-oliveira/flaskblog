# Flaskblog

## Setting Enviroments Variables on Linux/Max

	export FLASK_APP=flaskblog.py

## Setting Enviroments Variables on Windows

	set FLASK_APP=flaskblog.py

## Running the Application

	flask run
## Turning on the debug mode

	export FLASK_DEBUG=1

## Trees

### Flask Objects

There are Flask, render_template, url_for in flask module.

### Flask-wtf Objects

	flask_wtf >>> FlaskForm
	wtforms >>> StringField, PasswordField, SubmitField, BooleanField 
				validators >>> DataRequired, Length, Email, EqualTo

## How to Gerate Secrets Keys with Python

	import secrets
	secrets.token_hex(16)

## Getting flash messagem with jinja2

	{% with messages = get_flashed_messages(with_categories=true) %}
		<!-- DO STUFF -->
	{% endwith %}

## Checking if there is errors in a form validation with jinja2

	{% if form.username.errors %}
		<<!-- DO STUFF IF TRUE -->
	{% else %}
		<<!-- DO STUFF IF FALSE -->
	{% endif %}

## Query using SQLAlchemy

	User.query.all()
	User.query.filter_by(username='Myke').all()
	User.query.first()
	User.query.get(1)
