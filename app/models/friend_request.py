from .db import db

class Friend_Request(db.Model):
    __tablename__ = 'friend_requests'

    id = db.Column(db.Integer, primary_key=True)
    user_id_from = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_id_to = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    users = db.relationship('User', foreign_keys=[user_id_from, user_id_to])


    def to_dict(self):
        return {
            'id': self.id,
            'user_id_from': self.user_id_from,
            'user_id_to': self.user_id_to
        }
