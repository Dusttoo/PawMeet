from flask import Blueprint, jsonify, request
from app.models import Post, Comment, Like, db
from app.forms.add_post import PostForm

forum_routes = Blueprint('forums', __name__)

@forum_routes.route('/posts')
def posts():
    posts = Post.query.all()
    return {'posts': [post.to_dict() for post in posts]}


@forum_routes.route('/posts/add', methods=['POST'])
def add_post():
    if request.method == "POST":
        form = PostForm()
        form['csrf_token'].data = request.cookies['csrf_token']
        if form.validate_on_submit():
            data = Post()
            form.populate_obj(data)
            db.session.add(data)
            db.session.commit()
        return data.to_dict()


@forum_routes.route('/comments')
def comments():
    comments = Comment.query.all()
    return {'comments': [comment.to_dict() for comment in comments]}

@forum_routes.route('/likes')
def likes():
    likes = Like.query.all()
    return {'likes': [like.to_dict() for like in likes]}


