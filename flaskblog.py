from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '7a891c28f52a8d0a6540dbb06c3d2faa'

posts = [
	{
		'author': 'Myke Albuquerque Pinto de Oliveira',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'April 20, 2019'
	},
	{
		'author': 'Maria Caliente de las Dores',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'June 21, 2019'
	},
	{
		'author': 'Jane Doe',
		'title': 'Blog Post 3',
		'content': 'Third post content',
		'date_posted': 'July 18, 2019'
	}
]

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
	return render_template('home.html', posts=posts)

@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route('/register')
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
	form = RegistrationForm()
	return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
	app.run(debug=True)
