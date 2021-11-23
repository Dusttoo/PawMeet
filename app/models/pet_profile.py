from .db import db

class Pet_Profile(db.Model):
    __tablename__ = 'pet_profiles'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    profile_img = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    breed = db.Column(db.String, nullable=False)
    age= db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)


    users = db.relationship('User', back_populates='pet_profiles')
    pet_images = db.relationship(
        'Pet_Image', cascade="all, delete-orphan", back_populates='pet_profiles')

    def to_dict(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'profile_img': self.profile_img,
            'name': self.name,
            'breed': self.breed,
            'age': self.age,
            'description': self.description
        }