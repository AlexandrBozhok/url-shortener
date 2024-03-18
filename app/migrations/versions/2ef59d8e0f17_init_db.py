"""init_db

Revision ID: 2ef59d8e0f17
Revises: 
Create Date: 2024-03-18 21:06:27.831904

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ef59d8e0f17'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('links',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original_url', sa.String(length=512), nullable=False),
    sa.Column('short_url', sa.String(length=10), nullable=True),
    sa.Column('visits', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('links_pkey')),
    sa.UniqueConstraint('short_url', name=op.f('links_short_url_key'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('links')
    # ### end Alembic commands ###
