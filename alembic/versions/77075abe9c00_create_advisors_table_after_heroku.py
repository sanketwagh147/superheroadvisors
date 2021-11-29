"""create advisors table after heroku

Revision ID: 77075abe9c00
Revises: 36e31a0afd2a
Create Date: 2021-11-29 07:25:08.444356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77075abe9c00'
down_revision = '36e31a0afd2a'
branch_labels = None
depends_on = None



def upgrade():
     op.create_table("advisors",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("name", sa.String(), nullable=False),
                    sa.Column("image_url", sa.String(length=255), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True) , server_default=sa.text('now()'), nullable=False),
                    sa.Column('status', sa.Boolean(), server_default=sa.text('false'), nullable=False), 
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )


def downgrade():
    op.drop_table("advisors")