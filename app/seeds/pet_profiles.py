from app.models import db, Pet_Profile, Breed_Image, Breed
from faker import Faker
from random import randint, random, randrange

# get_breeds = Breed.query.all()
# breeds = {'breeds': [breed.to_dict() for breed in get_breeds]}

breeds = ['American Staffordshire Terrier', 'Beagle', 'Boxer', 'Bulldog', 'Cane Corso', 'Dachshund', 'French Bulldog', 'German Shepherd Dog',
    'German Shorthaired Pointer', 'Golden Retriever', 'Labrador Retriever', 'Pug', 'Rottweiler', 'Standard Poodle']

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
        num = breeds[randrange(1, 14)]
        print(num, breeds)
        i = Pet_Profile(
            owner_id=randrange(1, 12),
            profile_img=f'https://placedog.net/{randint(1, 1001)}',
            name=fake.name(),
            breed= num,
            age=randrange(1, 16),
            description=fake.paragraph()
        )

        db.session.add(i)

    db.session.commit()

def undo_pet_profiles():
    db.session.execute('TRUNCATE pet_profiles RESTART IDENTITY CASCADE;')
    db.session.commit()
