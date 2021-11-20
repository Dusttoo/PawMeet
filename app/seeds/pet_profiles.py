from app.models import db, Pet_Profile
from faker import Faker
from random import random, randrange

breeds = ['American Staffordshire Terrier', 'Beagle', 'Boxer', 'Bulldog', 'Cane Corso', 'Dachshund', 'French Bulldog', 'German Shepherd Dog', 'German Shorthaired Pointer', 'Golden Retriever', 'Labrador Retriever', 'Pug', 'Rottweiler', 'Standard Poodle']

def seed_pet_profiles():
    fake = Faker()
    callie = Pet_Profile(
        owner_id=1,
        profile_img='https://images.pexels.com/photos/2679612/pexels-photo-2679612.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        name='Callie',
        breed='Dachshund',
        age='1 year',
        description='Callie loves long walks on the beach and chasing flies. She is fierce, even though she is afraid of her own farts.'
    )

    db.session.add(callie)

    for i in range(1, 35):
        i = Pet_Profile(
            owner_id=randrange(1, 12),
            profile_img=f'https://placedog.net/{randrange(1,1001)}',
            name=fake.name(),
            breed=breeds[randrange(1, 14)],
            age=randrange(1, 16),
            description=fake.paragraph()
        )

        db.session.add(i)

    db.session.commit()

def undo_pet_profiles():
    db.session.execute('TRUNCATE pet_profiles RESTART IDENTITY CASCADE;')
    db.session.commit()
