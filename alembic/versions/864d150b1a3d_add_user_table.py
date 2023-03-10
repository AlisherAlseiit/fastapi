"""add user table

Revision ID: 864d150b1a3d
Revises: 749609cec5e9
Create Date: 2023-03-10 17:02:30.956191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '864d150b1a3d'
down_revision = '749609cec5e9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))


def downgrade() -> None:
    op.drop_table('users')
