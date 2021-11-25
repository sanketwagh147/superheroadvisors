""" Creating Advisor table

Revision ID: 25be962d8cf9
Revises: 
Create Date: 2021-11-25 23:08:41.097555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25be962d8cf9'
down_revision = None
branch_labels = None
depends_on = None




def upgrade():
    op.create_table("advisors",
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
    op.drop_table("advisors")
    pass