from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, email_validator
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')






class SignUpForm(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired(message='Username required'), username_exists, Length(min=6, max=18, message='Username must be between 6 and 18 characters')])
    email = StringField('email', validators=[
                        DataRequired(message='Email required'), user_exists, Email(message='Please enter a valid email')])
    password = StringField('password', validators=[DataRequired(message='Password required'), Length(
        min=6, max=18, message='Password must be between 6 and 18 characters')])
    # repeat_password = StringField('password', validators=[DataRequired(
    #     message='Password required')])
    first_name = StringField('first_name', validators=[DataRequired(message='First Name Required'), Length(
        min=3, max=18, message='First Name must be between 3 and 18 characters')])
    last_name = StringField('last_name', validators=[DataRequired(message='Last Name Required'), Length(
        min=3, max=18, message='Last Name must be between 3 and 18 characters')])
    profile_img = StringField('profile_img', validators=[DataRequired(message='Profile Image URL Required')])
    barking_since = StringField('barking_since', validators=[
                                DataRequired()])
