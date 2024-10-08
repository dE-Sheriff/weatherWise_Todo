"""Added new fields to Task model

Revision ID: 2ef3ced7490b
Revises: 
Create Date: 2024-08-31 22:15:06.451278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ef3ced7490b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('start_date', sa.Date(), nullable=False))
        batch_op.add_column(sa.Column('start_time', sa.Time(), nullable=False))
        batch_op.add_column(sa.Column('end_date', sa.Date(), nullable=True))
        batch_op.add_column(sa.Column('end_time', sa.Time(), nullable=True))
        batch_op.add_column(sa.Column('location', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('suggested_by_app', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('remark', sa.String(length=255), nullable=True))
        batch_op.drop_column('due_date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('due_date', sa.DATETIME(), nullable=False))
        batch_op.drop_column('remark')
        batch_op.drop_column('suggested_by_app')
        batch_op.drop_column('location')
        batch_op.drop_column('end_time')
        batch_op.drop_column('end_date')
        batch_op.drop_column('start_time')
        batch_op.drop_column('start_date')

    # ### end Alembic commands ###
