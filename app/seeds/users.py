from app.models import db, User
from faker import Faker

# Adds a demo user, you can add other users here if you want
def seed_users():
    fake = Faker()
    demo = User(
        username='Demo', 
        email='demo@aa.io', 
        password='password',
        first_name='Demo',
        last_name='User',
        barking_since='10-05-2021',
        profile_img='https://images.pexels.com/photos/2253275/pexels-photo-2253275.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')

    marnie = User(
        username='Marnie123',
        email='marnie@aa.io',
        password='password',
        first_name='Marnie',
        last_name='Matheson',
        barking_since='05-06-2021',
        profile_img='https://images.pexels.com/photos/243914/pexels-photo-243914.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')

    joe = User(
        username='JoeJoe',
        email='joe@aa.io',
        password='password',
        first_name='Joe',
        last_name='Jobilie',
        barking_since='11-11-2021',
        profile_img='https://images.pexels.com/photos/3610168/pexels-photo-3610168.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')

    tom = User(
        username='Tommy',
        email='tom@aa.io',
        password='password',
        first_name='Tom',
        last_name='Ford',
        barking_since='03-25-2020',
        profile_img='https://images.pexels.com/photos/1851164/pexels-photo-1851164.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')

    fake1 = User(
        username=fake.user_name(),
        email=fake.email(),
        password=fake.password(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        barking_since=fake.date_between(start_date='-3y', end_date='today'),
        profile_img='https://placeimg.com/640/480/any')

    fake2 = User(
        username=fake.user_name(),
        email=fake.email(),
        password=fake.password(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        barking_since=fake.date_between(start_date='-3y', end_date='today'),
        profile_img='https://placeimg.com/640/480/animals')

    fake3 = User(
        username=fake.user_name(),
        email=fake.email(),
        password=fake.password(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        barking_since=fake.date_between(start_date='-3y', end_date='today'),
        profile_img='https://placeimg.com/640/480/architecture')

    fake4 = User(
        username=fake.user_name(),
        email=fake.email(),
        password=fake.password(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        barking_since=fake.date_between(start_date='-3y', end_date='today'),
        profile_img='https://placeimg.com/640/480/nature')

    fake5 = User(
        username=fake.user_name(),
        email=fake.email(),
        password=fake.password(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        barking_since=fake.date_between(start_date='-3y', end_date='today'),
        profile_img='https://placeimg.com/640/480/people')
    fake6 = User(
        username=fake.user_name(),
        email=fake.email(),
        password=fake.password(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        barking_since=fake.date_between(start_date='-3y', end_date='today'),
        profile_img='https://placeimg.com/640/480/tech')
    fake7 = User(
        username=fake.user_name(),
        email=fake.email(),
        password=fake.password(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        barking_since=fake.date_between(start_date='-3y', end_date='today'),
        profile_img='https://placeimg.com/640/480/sepia')
    
    


    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(joe)
    db.session.add(tom)
    db.session.add(fake1)
    db.session.add(fake2)
    db.session.add(fake3)
    db.session.add(fake4)
    db.session.add(fake5)
    db.session.add(fake6)
    db.session.add(fake7)




    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
