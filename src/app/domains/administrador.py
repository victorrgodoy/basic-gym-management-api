import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.domain.usuario import Usuario, TipoUsuario 

class Administrador(Usuario):
    __tablename__ = "administrador"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("usuario.id"), primary_key=True
    )

    __mapper_args__ = {
        "polymorphic_identity": TipoUsuario.ADMINISTRADOR 
    }