from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class FriendListForm(FlaskForm):
    current_user_id = IntegerField('current_user_id', validators=[DataRequired()])
    friend_user_id = IntegerField('friend_user_id', validators=[DataRequired()])
    is_following = BooleanField('is_following')