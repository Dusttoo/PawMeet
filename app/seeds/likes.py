from app.models import db, Like
from faker import Faker
from random import randrange


def seed_likes():
    fake = Faker()
    like1 = Like(
        user_id=2,
        post_id=1,
    )

    like2 = Like(
        user_id=1,
        post_id=2,
    )

    db.session.add(like1)
    db.session.add(like2)

    for i in range(20):
        i = Like(
            user_id=randrange(1, 12),
            post_id=randrange(1, 202),
        )
        db.session.add(i)
    

    db.session.commit()


def undo_likes():
    db.session.execute('TRUNCATE likes RESTART IDENTITY CASCADE;')
    db.session.commit()
