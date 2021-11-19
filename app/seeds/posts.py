from app.models import db, Post
import datetime


def seed_posts():
    post1 = Post(
        user_id = 1,
        title = 'Is this normal?',
        post_body = 'My dog is always chasing his tail. Is this normal beahvior?',
        posted='11-11-2021',
        group_id=7
    )

    post2 = Post(
        user_id=2,
        title='Dobermans are the best!',
        post_body='I just wanted to say that Dobermans are, by far, the BEST breed!!!',
        posted='11-05-2021',
        group_id=3

    )

    db.session.add(post1)
    db.session.add(post2)

    db.session.commit()


def undo_posts():
    db.session.execute('TRUNCATE posts RESTART IDENTITY CASCADE;')
    db.session.commit()
