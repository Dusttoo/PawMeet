from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired
from app.models import User_Answer


class UserAnswerForm(FlaskForm):
    user_id = IntegerField('user_id', validators=[DataRequired()])
    trait_id = IntegerField('trait_id', validators=[DataRequired()])
    answer = IntegerField('answer', validators=[DataRequired()])
    important = BooleanField('important')
