import uuid

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.database import Base


class Exercicio(Base):
    __tablename__ = "exercicio"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True
    )

    descricao: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    itens_treino: Mapped[list["ItemTreino"]] = relationship(
        "ItemTreino",
        back_populates="exercicio"
    )

    def alterar_descricao(self, nova_descricao: str) -> None:
        if not nova_descricao or not nova_descricao.strip():
            raise ValueError("A descrição do exercício não pode ser vazia.")

        if len(nova_descricao) > 500:
            raise ValueError("A descrição não pode ter mais de 500 caracteres.")

        self.descricao = nova_descricao.strip()