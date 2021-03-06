"""empty message

Revision ID: fc390be10fc4
Revises: 309363f673e8
Create Date: 2021-11-22 10:44:18.211252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc390be10fc4'
down_revision = '309363f673e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('breed_traits', sa.Column('min', sa.String(), nullable=False))
    op.add_column('breed_traits', sa.Column('max', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('breed_traits', 'max')
    op.drop_column('breed_traits', 'min')
    # ### end Alembic commands ###
