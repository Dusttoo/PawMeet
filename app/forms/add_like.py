from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from app.models import Like


class LikeForm(FlaskForm):
    post_id = IntegerField('post_id', validators=[DataRequired()])
    user_id = IntegerField('user_id', validators=[DataRequired()])

    
