from .db import db


class Friends_List(db.Model):
    __tablename__ = 'friends_list'

    id = db.Column(db.Integer, primary_key=True)
    current_user_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    friend_user_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    is_following = db.Column(db.Boolean, default=False, nullable=False)

    users = db.relationship('User', back_populates='friend_requests')

    def to_dict(self):
        return {
            'id': self.id,
            'current_user_id': self.current_user_id,
            'friend_user_id': self.friend_user_id,
            'is_following': self.is_following
        }
