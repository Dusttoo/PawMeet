from .db import db


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    comment_body = db.Column(db.Text, nullable=False)
    posted = db.Column(db.Date, nullable=False)


    users = db.relationship('User', back_populates='comments')
    posts = db.relationship('Post', back_populates='comments')


    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'post_body': self.post_body,
            'posted': self.posted

        }
