"""empty message

Revision ID: 8867055b291c
Revises: 36a1771dc961
Create Date: 2020-05-14 11:31:19.504004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8867055b291c'
down_revision = '36a1771dc961'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('link',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original_url', sa.String(length=512), nullable=True),
    sa.Column('short_url', sa.String(length=5), nullable=True),
    sa.Column('visits', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('link')
    # ### end Alembic commands ###
