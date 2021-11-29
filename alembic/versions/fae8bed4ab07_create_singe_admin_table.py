"""create singe admin table

Revision ID: fae8bed4ab07
Revises: 1b269e4c47b9
Create Date: 2021-11-27 13:24:18.762719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fae8bed4ab07'
down_revision = '1b269e4c47b9'
branch_labels = None
depends_on = None


def upgrade():
    # op.create_table("admin",
    #                 sa.Column("id", sa.Integer(), nullable=False),
    #                 sa.Column("name", sa.String(), nullable=False),
    #                 sa.Column("image_url", sa.String(length=255), nullable=False),
    #                 sa.Column("created_at", sa.TIMESTAMP(timezone=True) ,
    #                         server_default=sa.text('now()'), nullable=False),
    #                 sa.PrimaryKeyConstraint('id'),
    #                 sa.UniqueConstraint('name')
    #                 )
    pass


def downgrade():
    # op.drop_table("admin")
    pass