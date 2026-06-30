import uuid

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.database import Base


class FichaTreino(Base):
    __tablename__ = "ficha_treino"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    objetivo: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    aluno_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("aluno.id"),
        nullable=False
    )

    instrutor_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("instrutor.id"),
        nullable=False
    )

    aluno: Mapped["Aluno"] = relationship(
        "Aluno",
        back_populates="fichas_treino"
    )

    instrutor: Mapped["Instrutor"] = relationship(
        "Instrutor",
        back_populates="fichas_treino"
    )

    itens_treino: Mapped[list["ItemTreino"]] = relationship(
        "ItemTreino",
        back_populates="ficha_treino",
        cascade="all, delete-orphan"
    )

    def alterar_objetivo(self, novo_objetivo: str) -> None:
        if not novo_objetivo or not novo_objetivo.strip():
            raise ValueError("O objetivo da ficha não pode ser vazio.")

        if len(novo_objetivo) > 200:
            raise ValueError("O objetivo não pode ter mais de 200 caracteres.")

        self.objetivo = novo_objetivo.strip()