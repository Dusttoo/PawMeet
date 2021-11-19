"""empty message

Revision ID: d2bc612233b0
Revises: cb85a9bda95c
Create Date: 2021-11-19 07:28:17.928959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2bc612233b0'
down_revision = 'cb85a9bda95c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('group_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'group_id')
    # ### end Alembic commands ###
