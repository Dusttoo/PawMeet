from .db import db

class Breed_Trait(db.Model):
    __tablename__ = 'breed_traits'

    id = db.Column(db.Integer, primary_key=True)
    trait = db.Column(db.String, nullable=False)
    question = db.Column(db.String, nullable=False)
    min = db.Column(db.String, nullable=False)
    max = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)

    breed_answers = db.relationship('Breed_Answer', back_populates='breed_traits')
    user_answers = db.relationship('User_Answer', back_populates='breed_traits')


    def to_dict(self):
        return {
            'id': self.id,
            'trait': self.trait,
            'question': self.question,
            'min': self.min,
            'max': self.max,
            'description': self.description

        }
