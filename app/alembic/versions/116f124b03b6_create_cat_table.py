"""create cat table

Revision ID: 116f124b03b6
Revises: 
Create Date: 2023-04-10 18:50:09.304736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '116f124b03b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'cats',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('color', sa.String(50), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('cats')
    
