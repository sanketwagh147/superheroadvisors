"""Create user table

Revision ID: 9a303c044da0
Revises: ae6c94977125
Create Date: 2021-11-26 17:20:36.302098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a303c044da0'
down_revision = 'ae6c94977125'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table("users",
                    sa.Column("name", sa.String(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True) ,
                            server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('email'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table("users")
    pass

