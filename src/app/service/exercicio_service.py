import uuid

from typing import Optional

from app.domain.exercicio import Exercicio
from app.repository.exercicio_repository import ExercicioRepository


class ExercicioService:

    def __init__(self, exercicio_repository: ExercicioRepository):
        self.__exercicio_repository = exercicio_repository

    def find_by_id(
        self,
        exercicio_id: uuid.UUID
    ) -> Optional[Exercicio]:
        return self.__exercicio_repository.find_by_id(exercicio_id)

    def read(self) -> list[Exercicio]:
        return self.__exercicio_repository.read()

    def create(self, exercicio: Exercicio) -> Exercicio:
        exercicio_existente = self.__exercicio_repository.find_by_nome(
            exercicio.nome
        )

        if exercicio_existente:
            raise ValueError(
                "Já existe um exercício cadastrado com esse nome."
            )

        return self.__exercicio_repository.create(exercicio)

    def update(
        self,
        exercicio_id: uuid.UUID,
        nome: Optional[str] = None,
        descricao: Optional[str] = None
    ) -> Exercicio:
        exercicio = self.find_by_id(exercicio_id)

        if not exercicio:
            raise LookupError("Exercício não encontrado.")

        if nome is not None:
            exercicio_com_mesmo_nome = (
                self.__exercicio_repository.find_by_nome(nome)
            )

            if (
                exercicio_com_mesmo_nome
                and exercicio_com_mesmo_nome.id != exercicio.id
            ):
                raise ValueError(
                    "Já existe um exercício cadastrado com esse nome."
                )

            exercicio.alterar_nome(nome)

        if descricao is not None:
            exercicio.alterar_descricao(descricao)

        return self.__exercicio_repository.update(exercicio)

    def delete(self, exercicio_id: uuid.UUID) -> None:
        exercicio = self.find_by_id(exercicio_id)

        if not exercicio:
            raise LookupError("Exercício não encontrado.")

        self.__exercicio_repository.delete(exercicio)