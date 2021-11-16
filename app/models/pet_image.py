from .db import db

class Pet_Image(db.Model):
    __tablename__ = 'pet_images'

    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet_profiles.id'), nullable=False)
    img_url = db.Column(db.String, nullable=False)


    pet_profiles = db.relationship('Pet_Profile', back_populates='pet_images')

    def to_dict(self):
        return {
            'id': self.id,
            'pet_id': self.pet_id,
            'img_url': self.img_url
        }