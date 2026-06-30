import uuid

from abc import ABC, abstractmethod
from typing import Optional

from app.domain.item_treino import ItemTreino


class ItemTreinoRepository(ABC):

    @abstractmethod
    def find_by_id(
        self,
        item_treino_id: uuid.UUID
    ) -> Optional[ItemTreino]:
        pass

    @abstractmethod
    def find_by_ficha_treino_id(
        self,
        ficha_treino_id: uuid.UUID
    ) -> list[ItemTreino]:
        pass

    @abstractmethod
    def create(self, item_treino: ItemTreino) -> ItemTreino:
        pass

    @abstractmethod
    def update(self, item_treino: ItemTreino) -> ItemTreino:
        pass

    @abstractmethod
    def delete(self, item_treino: ItemTreino) -> None:
        pass