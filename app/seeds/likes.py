from app.models import db, Like
import datetime


def seed_likes():
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

    db.session.commit()


def undo_likes():
    db.session.execute('TRUNCATE likes RESTART IDENTITY CASCADE;')
    db.session.commit()
