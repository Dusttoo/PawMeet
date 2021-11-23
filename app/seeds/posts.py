from random import randrange
from app.models import db, Post
from faker import Faker



def seed_posts():
    fake = Faker()
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

    for i in range(200):

        i = Post(
            user_id=randrange(1, 12),
            title=fake.sentence(),
            post_body=fake.paragraph(),
            posted=fake.date_between(start_date='-3y', end_date='today'),
            group_id=randrange(1, 8)

        )
        db.session.add(i)

   
    db.session.commit()


def undo_posts():
    db.session.execute('TRUNCATE posts RESTART IDENTITY CASCADE;')
    db.session.commit()
