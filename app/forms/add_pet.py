from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from app.models import Pet_Profile


class PetForm(FlaskForm):
    user_id = IntegerField('user_id', validators=[DataRequired()])
    profile_img = StringField('profile_img', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    breed = StringField('breed', validators=[DataRequired()])
    age = StringField('age', validators=[DataRequired()])
    description = StringField('age', validators=[DataRequired()])

