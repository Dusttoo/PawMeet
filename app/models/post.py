from .db import db

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String, nullable=False)
    post_body = db.Column(db.Text, nullable=False)
    posted = db.Column(db.String, nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('breed_groups.id'), nullable=True)

    users = db.relationship('User', back_populates='posts')
    comments = db.relationship('Comment', cascade="all, delete-orphan", back_populates='posts')
    likes = db.relationship('Like', cascade="all, delete-orphan", back_populates='posts')
    breed_groups = db.relationship('Breed_Group', back_populates='posts')


    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'post_body': self.post_body,
            'posted': self.posted,
            'group_id': self.group_id
        }

    
