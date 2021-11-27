from app.models import db, User
from faker import Faker
from random import randint, random, randrange


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
        profile_img=f'https://i.pravatar.cc/150?u=demo@aa.io')

    marnie = User(
        username='Marnie123',
        email='marnie@aa.io',
        password='password',
        first_name='Marnie',
        last_name='Matheson',
        barking_since='05-06-2021',
        profile_img=f'https://i.pravatar.cc/150?u=joe@aa.io')

    joe = User(
        username='JoeJoe',
        email='joe@aa.io',
        password='password',
        first_name='Joe',
        last_name='Jobilie',
        barking_since='11-11-2021',
        profile_img=f'https://i.pravatar.cc/150?u=joe@aa.io')

    tom = User(
        username='Tommy',
        email='tom@aa.io',
        password='password',
        first_name='Tom',
        last_name='Ford',
        barking_since='03-25-2020',
        profile_img=f'https://i.pravatar.cc/150?u=tom@aa.io')

    for i in range(1, 12):
        email = fake.email()
        i = User(
            username=fake.user_name(),
            email=email,
            password=fake.password(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            barking_since=fake.date_between(
                start_date='-3y', end_date='today'),
            profile_img=f'https://i.pravatar.cc/150?u={email}')

        db.session.add(i)


    

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(joe)
    db.session.add(tom)





    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
