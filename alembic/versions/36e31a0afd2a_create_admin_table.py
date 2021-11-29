"""create admin table

Revision ID: 36e31a0afd2a
Revises: 54b6c75634f1
Create Date: 2021-11-29 07:18:04.492767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36e31a0afd2a'
down_revision = '54b6c75634f1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("admin",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("name", sa.String(), nullable=False),
                    sa.Column("image_url", sa.String(length=255), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True) ,
                            server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name'))

def downgrade():
    op.drop_table("admin")
    pass
