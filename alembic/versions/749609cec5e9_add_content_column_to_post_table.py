"""add content column to post table

Revision ID: 749609cec5e9
Revises: df0bc9d6a4a5
Create Date: 2023-03-10 16:49:31.328382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '749609cec5e9'
down_revision = 'df0bc9d6a4a5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    


def downgrade() -> None:
    op.drop_column("posts", 'content')
