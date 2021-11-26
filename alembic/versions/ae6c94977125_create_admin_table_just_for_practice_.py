"""Create admin table just for practice and enter 1 admin manually

Revision ID: ae6c94977125
Revises: 25be962d8cf9
Create Date: 2021-11-26 13:57:05.351113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae6c94977125'
down_revision = '25be962d8cf9'
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
                    sa.UniqueConstraint('name')
                    )
    pass


def downgrade():
    op.drop_table("admin")
    pass