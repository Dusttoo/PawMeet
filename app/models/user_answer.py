from .db import db

class User_Answer(db.Model):
    __tablename__ = "user_answers"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    trait_id = db.Column(db.Integer, db.ForeignKey('breed_traits.id'), nullable=False)
    answer = db.Column(db.Integer, nullable=False)
    # important = db.Column(db.Boolean, default=False)

    users = db.relationship('User', back_populates='user_answers')
    breed_traits = db.relationship('Breed_Trait', back_populates='user_answers')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'trait_id': self.trait_id,
            'answer': self.answer,
            # 'important': self.important
        }
