import uuid
from datetime import datetime
from typing import Optional
from app.config.database import Base
from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

class CheckIn(Base):
    __tablename__ = 'check_in'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    aluno_id = Column(UUID(as_uuid=True), ForeignKey('aluno.id', ondelete='CASCADE'), nullable=False)
    data_hora = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, aluno_id: uuid.UUID, data_hora: Optional[datetime] = None):
        self.id = uuid.uuid4()
        self.aluno_id = aluno_id
        self.data_hora = data_hora or datetime.utcnow()