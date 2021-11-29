"""create advisor table

Revision ID: 1b269e4c47b9
Revises: 
Create Date: 2021-11-27 13:21:01.157170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b269e4c47b9'
down_revision = None
branch_labels = None
depends_on = None



def upgrade():
    pass
    #f56b816e0d8573f75e699e0d33349e5ef16f137c82fe95da2f53469255549653 op.create_table("advisors",
    #                 sa.Column("id", sa.Integer(), nullable=False),
    #                 sa.Column("name", sa.String(), nullable=False),
    #                 sa.Column("image_url", sa.String(length=255), nullable=False),
    #                 sa.Column("created_at", sa.TIMESTAMP(timezone=True) ,
    #                         server_default=sa.text('now()'), nullable=False),
    #                 sa.PrimaryKeyConstraint('id'),
    #                 sa.UniqueConstraint('name')
    #                 )
    # pass


def downgrade():
    # op.drop_table("advisors")
    pass