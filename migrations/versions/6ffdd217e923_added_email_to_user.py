"""added email to user

Revision ID: 6ffdd217e923
Revises: 7a02f939cb20
Create Date: 2021-07-09 18:21:44.477113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ffdd217e923'
down_revision = '7a02f939cb20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    # ### end Alembic commands ###