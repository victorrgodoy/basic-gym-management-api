import uuid
from sqlalchemy import ForeignKey, String 
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.domain.usuario import Usuario, TipoUsuario 

class Instrutor(Usuario):
    __tablename__ = "instrutor"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("usuario.id"), primary_key=True
    )
    cref: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)

    fichas_treino: Mapped[list["FichaTreino"]] = relationship(
        "FichaTreino",
        back_populates="instrutor"
    )

    __mapper_args__ = {
        "polymorphic_identity": TipoUsuario.INSTRUTOR 
    }