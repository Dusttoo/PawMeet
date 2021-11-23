from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Post

class PostForm(FlaskForm):
    user_id = IntegerField('user_id', validators=[DataRequired()])
    title = StringField('title', validators=[DataRequired(message='Title Required')])
    post_body = StringField('post_body', validators=[DataRequired(message='Body required')])
    posted = StringField('posted', validators=[DataRequired()])
    group_id = IntegerField('group_id', validators=[DataRequired()])


