import uuid

from typing import Optional

from app.domain.item_treino import ItemTreino
from app.repository.exercicio_repository import ExercicioRepository
from app.repository.ficha_treino_repository import FichaTreinoRepository
from app.repository.item_treino_repository import ItemTreinoRepository


class ItemTreinoService:

    def __init__(
        self,
        item_treino_repository: ItemTreinoRepository,
        ficha_treino_repository: FichaTreinoRepository,
        exercicio_repository: ExercicioRepository
    ):
        self.__item_treino_repository = item_treino_repository
        self.__ficha_treino_repository = ficha_treino_repository
        self.__exercicio_repository = exercicio_repository

    def find_by_id(
        self,
        item_treino_id: uuid.UUID
    ) -> Optional[ItemTreino]:
        return self.__item_treino_repository.find_by_id(
            item_treino_id
        )

    def read_by_ficha_treino(
        self,
        ficha_treino_id: uuid.UUID
    ) -> list[ItemTreino]:
        self.__validar_ficha_treino(ficha_treino_id)

        return self.__item_treino_repository.find_by_ficha_treino_id(
            ficha_treino_id
        )

    def create(self, item_treino: ItemTreino) -> ItemTreino:
        self.__validar_ficha_treino(item_treino.ficha_treino_id)
        self.__validar_exercicio(item_treino.exercicio_id)

        return self.__item_treino_repository.create(item_treino)

    def update(
        self,
        item_treino_id: uuid.UUID,
        exercicio_id: uuid.UUID | None = None,
        series: int | None = None,
        repeticoes: int | None = None,
        observacao: str | None = None,
        atualizar_observacao: bool = False
    ) -> ItemTreino:
        item_treino = self.find_by_id(item_treino_id)

        if not item_treino:
            raise LookupError("Item de treino não encontrado.")

        if exercicio_id is not None:
            self.__validar_exercicio(exercicio_id)
            item_treino.exercicio_id = exercicio_id

        precisa_atualizar_execucao = (
            series is not None
            or repeticoes is not None
            or atualizar_observacao
        )

        if precisa_atualizar_execucao:
            novas_series = (
                series
                if series is not None
                else item_treino.series
            )

            novas_repeticoes = (
                repeticoes
                if repeticoes is not None
                else item_treino.repeticoes
            )

            nova_observacao = (
                observacao
                if atualizar_observacao
                else item_treino.observacao
            )

            item_treino.alterar_execucao(
                series=novas_series,
                repeticoes=novas_repeticoes,
                observacao=nova_observacao
            )

        return self.__item_treino_repository.update(item_treino)

    def delete(self, item_treino_id: uuid.UUID) -> None:
        item_treino = self.find_by_id(item_treino_id)

        if not item_treino:
            raise LookupError("Item de treino não encontrado.")

        self.__item_treino_repository.delete(item_treino)

    def __validar_ficha_treino(
        self,
        ficha_treino_id: uuid.UUID
    ) -> None:
        ficha_treino = self.__ficha_treino_repository.find_by_id(
            ficha_treino_id
        )

        if not ficha_treino:
            raise LookupError("Ficha de treino não encontrada.")

    def __validar_exercicio(
        self,
        exercicio_id: uuid.UUID
    ) -> None:
        exercicio = self.__exercicio_repository.find_by_id(exercicio_id)

        if not exercicio:
            raise LookupError("Exercício não encontrado.")