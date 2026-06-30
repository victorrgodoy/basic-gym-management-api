import uuid

from abc import ABC, abstractmethod
from typing import Optional

from app.domain.exercicio import Exercicio


class ExercicioRepository(ABC):

    @abstractmethod
    def find_by_id(
        self,
        exercicio_id: uuid.UUID
    ) -> Optional[Exercicio]:
        pass

    @abstractmethod
    def find_by_nome(self, nome: str) -> Optional[Exercicio]:
        pass

    @abstractmethod
    def create(self, exercicio: Exercicio) -> Exercicio:
        pass

    @abstractmethod
    def read(self) -> list[Exercicio]:
        pass

    @abstractmethod
    def update(self, exercicio: Exercicio) -> Exercicio:
        pass

    @abstractmethod
    def delete(self, exercicio: Exercicio) -> None:
        pass