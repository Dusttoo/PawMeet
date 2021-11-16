from app.models import db, Pet_Profile

def seed_pet_profiles():
    callie = Pet_Profile(
        owner_id=1,
        profile_img='https://images.pexels.com/photos/2679612/pexels-photo-2679612.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        name='Callie',
        breed='Dachshund',
        age='1 year',
        description='Callie loves long walks on the beach and chasing flies. She is fierce, even though she is afraid of her own farts.'
    )

    db.session.add(callie)

    db.session.commit()

def undo_pet_profiles():
    db.session.execute('TRUNCATE pet_profiles RESTART IDENTITY CASCADE;')
    db.session.commit()
