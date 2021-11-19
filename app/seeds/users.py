from app.models import db, User
import datetime


# Adds a demo user, you can add other users here if you want
def seed_users():
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
