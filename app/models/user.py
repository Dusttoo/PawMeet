from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(55), nullable=False)
    barking_since = db.Column(db.String, nullable=False)
    profile_img = db.Column(db.String, nullable=False)

    comments = db.relationship('Comment', back_populates='users')
    pet_profiles = db.relationship('Pet_Profile', back_populates='users')
    posts = db.relationship('Post', back_populates='users')
    user_answers = db.relationship('User_Answer', back_populates='users')
    likes = db.relationship('Like', back_populates='users')
    user1 = db.relationship('Friend_Request', foreign_keys='Friend_Request.user_id_from', back_populates='users')
    user2 = db.relationship(
        'Friend_Request', foreign_keys='Friend_Request.user_id_to', back_populates='users')
    friend1 = db.relationship(
        'Friends_List', foreign_keys='Friends_List.current_user_id', back_populates='users')
    friend2 = db.relationship(
        'Friends_List', foreign_keys='Friends_List.friend_user_id', back_populates='users')
    message_to = db.relationship(
        'Message', foreign_keys='Message.user_id_to', back_populates='users')
    message_from = db.relationship(
        'Message', foreign_keys='Message.user_id_from', back_populates='users')


    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'barking_since': self.barking_since,
            'profile_img': self.profile_img
        }
