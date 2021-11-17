from app.models import db, Comment
import datetime


def seed_comments():
    comment1 = Comment(
        user_id= 2,
        post_id = 1,
        comment_body="Yes, that's totally normal! My dog does it too",
        posted='11-10-2021'
    )

    comment2 = Comment(
        user_id= 1,
        post_id = 2,
        comment_body='I have a Doberman too! He is awesome.',
        posted='11-10-2021'
    )

    db.session.add(comment1)
    db.session.add(comment2)

    db.session.commit()


def undo_comments():
    db.session.execute('TRUNCATE comments RESTART IDENTITY CASCADE;')
    db.session.commit()
