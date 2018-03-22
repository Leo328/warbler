from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from wtforms.widgets import TextArea


class UserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    name = StringField('name')
    email = StringField('email', validators=[DataRequired(), Email()])
    image_url = StringField('image_url')
    header_url = StringField('header_url')
    location = StringField('location')
    password = PasswordField('password', validators=[Length(min=6)])


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[Length(min=6)])
