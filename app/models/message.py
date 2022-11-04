from sqlalchemy.orm import backref
from .db import db

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    user_id_from = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_id_to = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    message = db.Column(db.String, nullable=False)
    
    users = db.relationship('User', foreign_keys=[user_id_from], backref='messages')
    users = db.relationship('User', foreign_keys=[
                            user_id_to], backref='messages')



    def to_dict(self):
        return {
            'id': self.id,
            'user_id_from': self.user_id_from,
            'user_id_to': self.user_id_to,
            'message': self.message
        }
