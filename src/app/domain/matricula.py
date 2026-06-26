import uuid
from datetime import date  
from sqlalchemy import Boolean, Date, ForeignKey 
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship 
from app.config.database import Base  
from app.domain.aluno import Aluno

class Matricula(Base):  
    __tablename__ = "matricula"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    data_inicio: Mapped[date] = mapped_column(Date, nullable=False)
    ativo: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    aluno_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("aluno.id"), nullable=False)

    aluno: Mapped[Aluno] = relationship("Aluno", back_populates="matriculas")
    
    def desativar_matricula(self) -> None:
        if not self.ativo:
            raise ValueError("A matrícula já está inativa.")
        self.ativo = False

    def ativar_matricula(self) -> None:
        if self.ativo:
            raise ValueError("A matrícula já está ativa.")
        self.ativo = True