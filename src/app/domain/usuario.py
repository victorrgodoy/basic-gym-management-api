import uuid
import re
from enum import Enum  
from sqlalchemy import String, Enum as SQLEnum 
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.config.database import Base

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

class TipoUsuario(str, Enum):
    ADMINISTRADOR = "administrador"
    INSTRUTOR = "instrutor"
    ALUNO = "aluno"

class Usuario(Base):
    __tablename__ = "usuario"
    __allow_unmapped__ = True

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(String(100), nullable=False)
    tipo: Mapped[TipoUsuario] = mapped_column(SQLEnum(TipoUsuario), nullable=False)

    __mapper_args__ = {
        "polymorphic_on": tipo
    }

    def alterar_nome(self, novo_nome: str) -> None:
        if not novo_nome:
            raise ValueError("O nome não pode ser vazio.")
        if len(novo_nome) > 100:
            raise ValueError("O nome não pode ter mais de 100 caracteres.")
        if not all(c.isalpha() or c.isspace() for c in novo_nome):
            raise ValueError("O nome deve conter apenas letras e espaços.")
        self.nome = novo_nome

    def alterar_email(self, novo_email: str) -> None:
        if not novo_email or not EMAIL_REGEX.match(novo_email):
            raise ValueError("Email inválido.")
        if len(novo_email) > 100:
            raise ValueError("O email não pode ter mais de 100 caracteres.")
        self.email = novo_email

    def alterar_senha(self, nova_senha: str) -> None:
        if not nova_senha or len(nova_senha) < 6:
            raise ValueError("A senha deve ter pelo menos 6 caracteres.")
        self.senha = nova_senha