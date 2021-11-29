"""adding status column to advisors

Revision ID: 3c812531be42
Revises: 2863feb07754
Create Date: 2021-11-28 10:40:09.029211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c812531be42'
down_revision = '2863feb07754'
branch_labels = None
depends_on = None


def upgrade():
    pass

    #f56b816e0d8573f75e699e0d33349e5ef16f137c82fe95da2f53469255549653s op.add_column('advisors', sa.Column(
    #                                     'status', 
    #                                     sa.Boolean(), 
    #                                     server_default=sa.text('false'),
    #                                     nullable=False 
    #                                 ))


def downgrade():
    pass
    # op.drop_column('advisors', 'status')