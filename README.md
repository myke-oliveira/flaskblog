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
