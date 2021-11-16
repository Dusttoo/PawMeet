from flask import Blueprint, jsonify
from app.models import Post, Comment, Like

forum_routes = Blueprint('forums', __name__)

@forum_routes.route('/posts')
def posts():
    posts = Post.query.all()
    return {'posts': [post.to_dict() for post in posts]}

@forum_routes.route('/comments')
def comments():
    comments = Comment.query.all()
    return {'comments': [comment.to_dict() for comment in comments]}

@forum_routes.route('/likes')
def likes():
    likes = Like.query.all()
    return {'likes': [like.to_dict() for like in likes]}


