"""create_table_check_in

Revision ID: afd2d9395a77
Revises: aefa80d31572
Create Date: 2026-06-29 11:59:32.014147

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'afd2d9395a77'
down_revision: Union[str, None] = 'aefa80d31572'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'check_in',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('aluno_id', sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(['aluno_id'], ['aluno.id'], ondelete='CASCADE'),
        sa.Column('data_hora', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('check_in')
