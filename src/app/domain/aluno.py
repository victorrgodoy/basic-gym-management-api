from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.domain.matricula import Matricula
import uuid
from sqlalchemy import String, ForeignKey  
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship 
from app.domain.usuario import Usuario, TipoUsuario 
from app.domain.matricula import Matricula

class Aluno(Usuario):
    __tablename__ = "aluno"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("usuario.id"), primary_key=True
    )
    cpf: Mapped[str] = mapped_column(String(14), nullable=False, unique=True)
    telefone: Mapped[str] = mapped_column(String(15), nullable=False)
    
    matriculas: Mapped[list[Matricula]] = relationship("Matricula",back_populates="aluno")

    __mapper_args__ = {
        "polymorphic_identity": TipoUsuario.ALUNO
    }

    def alterar_telefone(self, novo_telefone: str):
        if not novo_telefone:
            raise ValueError("Telefone não pode ser nulo ou vazio.")
        if len(novo_telefone) > 15:
            raise ValueError("Telefone não pode ter mais de 15 caracteres.")
        self.telefone = novo_telefone