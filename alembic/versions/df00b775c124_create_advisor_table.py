"""create advisor table

Revision ID: df00b775c124
Revises: 
Create Date: 2021-11-25 19:08:47.031570

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_utils import URLType

# revision identifiers, used by Alembic.
revision = 'df00b775c124'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("advisors",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("advisor", sa.String(), nullable=False),
                    sa.Column("image_url", URLType(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True) ,
                            server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('advisor')
                    )
    pass


def downgrade():
    op.drop_table("advisors")
    pass

