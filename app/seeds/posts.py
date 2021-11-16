from app.models import db, Post
import datetime


def seed_posts():
    post1 = Post(
        user_id = 1,
        title = 'Is this normal?',
        post_body = 'My dog is always chasing his tail. Is this normal beahvior?',
        posted=datetime.date.today().strftime("%b %d %Y")
    )

    post2 = Post(
        user_id=2,
        title='Dobermans are the best!',
        post_body='I just wanted to say that Dobermans are, by far, the BEST breed!!!',
        posted=datetime.date.today()
    )

    db.session.add(post1)
    db.session.add(post2)

    db.session.commit()


def undo_posts():
    db.session.execute('TRUNCATE posts RESTART IDENTITY CASCADE;')
    db.session.commit()
