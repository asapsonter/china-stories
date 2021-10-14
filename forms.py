from flask_wtf import FlaskForm    
from wtforms import StringField , PasswordField, SubmitField, BooleanField    
from wtforms.validators import DataRequired, Email, EqualTo, Length, EqualTo , ValidationError


 
# validator is used to check if the field is empty or not
# string field is used for form step up
#Flask-WTF is a Flask extension that provides a simple interface for creating WTForms.


# RegistrationForm is a class that inherits from FlaskForm
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=3, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),])
    comfirm_password = PasswordField('comfirm_Password', validators=[DataRequired(),EqualTo('password')]) 
    # EqualTo is used to check if the password is the same as the comfirm_password
    submit = SubmitField('Sign up')
    
#class representing login form
class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password')
    remember = BooleanField('remember me')
    login = SubmitField('Login')
    
    
    
    

