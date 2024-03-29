from app.models import db, Friends_List
from faker import Faker
from random import randrange


def seed_lists():
    demo = Friends_List(
            current_user_id=1, friend_user_id=2,
            is_following = True
        )
    marnie = Friends_List(
            current_user_id=2, friend_user_id=1,
            is_following = True
        )
    db.session.add(demo)
    db.session.add(marnie)
    
    for i in range(20):
        follow = False
        if(i / 2 == 0):
            follow = True
        i = Friends_List(
            current_user_id=randrange(1, 12), friend_user_id=randrange(1, 12),
            is_following = follow
        )
        db.session.add(i)

    db.session.commit()


def undo_list():
    db.session.execute('TRUNCATE friends_list RESTART IDENTITY CASCADE;')
    db.session.commit()
