import uuid

from sqlalchemy import CheckConstraint, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.database import Base


class ItemTreino(Base):
    __tablename__ = "item_treino"

    __table_args__ = (
        CheckConstraint("series > 0", name="ck_item_treino_series_positivas"),
        CheckConstraint(
            "repeticoes > 0",
            name="ck_item_treino_repeticoes_positivas"
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    series: Mapped[int] = mapped_column(nullable=False)

    repeticoes: Mapped[int] = mapped_column(nullable=False)

    observacao: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    ficha_treino_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("ficha_treino.id"),
        nullable=False
    )

    exercicio_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("exercicio.id"),
        nullable=False
    )

    ficha_treino: Mapped["FichaTreino"] = relationship(
        "FichaTreino",
        back_populates="itens_treino"
    )

    exercicio: Mapped["Exercicio"] = relationship(
        "Exercicio",
        back_populates="itens_treino"
    )

    def alterar_execucao(
        self,
        series: int,
        repeticoes: int,
        observacao: str | None = None
    ) -> None:
        if series <= 0:
            raise ValueError("A quantidade de séries deve ser maior que zero.")

        if repeticoes <= 0:
            raise ValueError("A quantidade de repetições deve ser maior que zero.")

        if observacao and len(observacao) > 500:
            raise ValueError(
                "A observação não pode ter mais de 500 caracteres."
            )

        self.series = series
        self.repeticoes = repeticoes
        self.observacao = observacao