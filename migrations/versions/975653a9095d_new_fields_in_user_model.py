"""new fields in user model

Revision ID: 975653a9095d
Revises: b4d5b6b9cbf5
Create Date: 2020-01-20 16:36:19.571181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '975653a9095d'
down_revision = 'b4d5b6b9cbf5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
