import uuid

from sqlalchemy import Boolean, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.config.database import Base


class Aluno(Base):
    __tablename__ = "alunos"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    cpf: Mapped[str] = mapped_column(String(14), nullable=False, unique=True)
    ativo: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    def __init__(self, nome: str, email: str, cpf: str):
        self.id = uuid.uuid4()
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.ativo = True

    def get_id(self) -> uuid.UUID:
        return self.id

    def get_nome(self) -> str:
        return self.nome

    def get_email(self) -> str:
        return self.email

    def get_cpf(self) -> str:
        return self.cpf

    def is_ativo(self) -> bool:
        return self.ativo

    def alterar_nome(self, novo_nome: str) -> None:
        if not novo_nome:
            raise ValueError("O nome não pode ser vazio.")
        if len(novo_nome) > 100:
            raise ValueError("O nome não pode ter mais de 100 caracteres.")
        if not all(c.isalpha() or c.isspace() for c in novo_nome):
            raise ValueError("O nome deve conter apenas letras e espaços.")
        self.nome = novo_nome

    def alterar_email(self, novo_email: str) -> None:
        if not novo_email:
            raise ValueError("O email não pode ser vazio.")
        if len(novo_email) > 100:
            raise ValueError("O email não pode ter mais de 100 caracteres.")
        if "@" not in novo_email or "." not in novo_email:
            raise ValueError("O email deve conter '@' e '.'.")
        self.email = novo_email

    def desativar_matricula(self) -> None:
        if not self.ativo:
            raise ValueError("O aluno já está inativo.")
        self.ativo = False

    def ativar_matricula(self) -> None:
        if self.ativo:
            raise ValueError("O aluno já está ativo.")
        self.ativo = True