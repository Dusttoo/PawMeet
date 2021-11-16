from .db import db

class Breed_Answer(db.Model):
    __tablename__ = 'breed_answers'

    id = db.Column(db.Integer, primary_key=True)
    breed_id = db.Column(db.Integer, db.ForeignKey('breeds.id'), nullable=False)
    trait_id = db.Column(db.Integer, db.ForeignKey(
        'breed_traits.id'), nullable=False)
    answer = db.Column(db.Integer, nullable=False)

    breeds = db.relationship('Breed', back_populates='breed_answers')
    breed_traits = db.relationship('Breed_Trait', back_populates='breed_answers')
