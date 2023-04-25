"""add column owner

Revision ID: 59ef1f0852c0
Revises: 116f124b03b6
Create Date: 2023-04-10 21:00:34.971209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59ef1f0852c0'
down_revision = '116f124b03b6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('cats', sa.Column("owner", sa.String(50), default=None))
    


def downgrade() -> None:
    op.drop_column("cats", 'owner')
    
