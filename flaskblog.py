from flask import Flask,render_template,url_for,request, redirect, flash
from flask.templating import render_template_string
from flask_wtf import form
from wtforms.form import Form
from forms import RegistrationForm, LoginForm

app = Flask (__name__)


app.config['SECRET_KEY'] = '5522abcd8'

posts = [
    {
        'author': 'sam sonter',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'mel d sol',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'mel d sol',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'April 22, 2018'
    },
    {
        'author': 'aarga shemenge',
        'title': 'Blog Post 1',
        'content': 'Second post content',
        'date_posted': 'March 11, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Blog')    


@app.route('/about')
def about():
    return render_template('about.html', title='blog')

@app.route('/register', methods=['GET', 'POST'])
def register(): 
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
    


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
    