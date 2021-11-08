from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, TextAreaField
from flask_wtf import FlaskForm




class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
