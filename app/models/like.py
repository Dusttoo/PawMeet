from .db import db

class Like(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    value = db.Column(db.Integer, nullable=False, default=1)

    posts = db.relationship('Post', back_populates='likes')

    def to_dict(self):
        return {
            'id': self.id,
            'post_id': self.post_id,
            'value': self.value
        }
