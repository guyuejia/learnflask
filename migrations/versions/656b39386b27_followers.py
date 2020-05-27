"""followers

Revision ID: 656b39386b27
Revises: b0b4c9f6e2b4
Create Date: 2020-05-26 16:42:06.407270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '656b39386b27'
down_revision = 'b0b4c9f6e2b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
