from .db import db

class Breed(db.Model):
    __tablename__ = 'breeds'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    breed_group = db.Column(db.Integer, db.ForeignKey('breed_groups.id'), nullable=False)
    personality = db.Column(db.String, nullable=False)
    avg_height = db.Column(db.JSON, nullable=False)
    avg_weight = db.Column(db.JSON, nullable=False)
    avg_life_exp = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)

    breed_groups = db.relationship('Breed_Group', back_populates='breeds')
    breed_images = db.relationship('Breed_Image', back_populates='breeds')
    breed_answers = db.relationship('Breed_Answer', back_populates='breeds')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'breed_group': self.breed_group,
            'personality': self.personality,
            'avg_height': self.avg_height,
            'avg_weight': self.avg_weight,
            'avg_life_exp': self.avg_life_exp,
            'description': self.description
        }
