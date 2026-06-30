import uuid

from abc import ABC, abstractmethod
from typing import Optional

from app.domain.ficha_treino import FichaTreino


class FichaTreinoRepository(ABC):

    @abstractmethod
    def find_by_id(
        self,
        ficha_treino_id: uuid.UUID
    ) -> Optional[FichaTreino]:
        pass

    @abstractmethod
    def create(self, ficha_treino: FichaTreino) -> FichaTreino:
        pass

    @abstractmethod
    def read(self) -> list[FichaTreino]:
        pass

    @abstractmethod
    def update(self, ficha_treino: FichaTreino) -> FichaTreino:
        pass

    @abstractmethod
    def delete(self, ficha_treino: FichaTreino) -> None:
        pass