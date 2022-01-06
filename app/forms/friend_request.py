from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class AddFriendForm(FlaskForm):
    user_id_from = IntegerField('user_id_from', validators=[DataRequired()])
    user_id_to = IntegerField('user_id_to', validators=[DataRequired()])
