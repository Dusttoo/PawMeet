from app.models import db, Friend_Request
from faker import Faker
from random import randrange


def seed_requests():
    for i in range(20):
        i = Friend_Request(
            user_id_from=randrange(1, 12), user_id_to=randrange(1, 12)
        )
        db.session.add(i)

    db.session.commit()


def undo_requests():
    db.session.execute('TRUNCATE friend_requests RESTART IDENTITY CASCADE;')
    db.session.commit()
