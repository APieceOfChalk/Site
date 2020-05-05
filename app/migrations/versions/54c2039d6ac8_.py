"""empty message

Revision ID: 54c2039d6ac8
Revises: 32933ee371fa
Create Date: 2020-05-05 22:50:25.216668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54c2039d6ac8'
down_revision = '32933ee371fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('name', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'name')
    # ### end Alembic commands ###
