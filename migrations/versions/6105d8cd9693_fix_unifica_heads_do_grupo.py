"""fix: unifica heads do grupo

Revision ID: 6105d8cd9693
Revises: 6f66595d05da, afd2d9395a77
Create Date: 2026-06-30 14:32:18.747869

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6105d8cd9693'
down_revision: Union[str, None] = ('6f66595d05da', 'afd2d9395a77')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
