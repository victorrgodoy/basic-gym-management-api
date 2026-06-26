import uuid
from sqlalchemy import ForeignKey, String 
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.domain.usuario import Usuario, TipoUsuario 

class Instrutor(Usuario):
    __tablename__ = "instrutor"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("usuario.id"), primary_key=True
    )
    cref: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)

    __mapper_args__ = {
        "polymorphic_identity": TipoUsuario.INSTRUTOR 
    }