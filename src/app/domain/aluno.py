import uuid
from sqlalchemy import String, ForeignKey  
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship 
from app.domain.usuario import Usuario, TipoUsuario 

class Aluno(Usuario):
    __tablename__ = "aluno"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("usuario.id"), primary_key=True
    )
    cpf: Mapped[str] = mapped_column(String(14), nullable=False, unique=True)
    telefone: Mapped[str] = mapped_column(String(15), nullable=False)
    
    matriculas: Mapped[list["Matricula"]] = relationship("Matricula", back_populates="aluno")
    
    fichas_treino: Mapped[list["FichaTreino"]] = relationship(
        "FichaTreino",
        back_populates="aluno"
    )

    __mapper_args__ = {
        "polymorphic_identity": TipoUsuario.ALUNO
    }