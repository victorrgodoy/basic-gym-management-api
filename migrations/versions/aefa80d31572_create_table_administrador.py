"""create_table_administrador

Revision ID: aefa80d31572
Revises: 9117b35c9119
Create Date: 2026-06-28 00:16:37.532992

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'aefa80d31572'
down_revision: Union[str, None] = '9117b35c9119'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'administrador',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(['id'], ['usuario.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('administrador')