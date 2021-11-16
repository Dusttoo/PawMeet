from app.models import db, Pet_Image

def seed_pet_images():
    callie1 = Pet_Image(
        pet_id=1,
        img_url='https://images.pexels.com/photos/1139794/pexels-photo-1139794.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
    )

    callie2 = Pet_Image(
        pet_id=1,
        img_url='https://images.pexels.com/photos/1139795/pexels-photo-1139795.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
    )

    callie3 = Pet_Image(
        pet_id=1,
        img_url='https://images.pexels.com/photos/1975516/pexels-photo-1975516.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
    )
    callie4 = Pet_Image(
        pet_id=1,
        img_url='https://images.pexels.com/photos/3104708/pexels-photo-3104708.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
    )
    callie5 = Pet_Image(
        pet_id=1,
        img_url='https://images.pexels.com/photos/755380/pexels-photo-755380.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260'
    )

    db.session.add(callie1)
    db.session.add(callie2)
    db.session.add(callie3)
    db.session.add(callie4)
    db.session.add(callie5)

    db.session.commit()

def undo_pet_images():
    db.session.execute('TRUNCATE pet_images RESTART IDENTITY CASCADE;')
    db.session.commit()
