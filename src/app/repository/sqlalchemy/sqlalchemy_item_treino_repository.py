import uuid

from typing import Optional

from sqlalchemy.orm import Session

from app.domain.item_treino import ItemTreino
from app.repository.item_treino_repository import ItemTreinoRepository


class SqlAlchemyItemTreinoRepository(ItemTreinoRepository):

    def __init__(self, db: Session):
        self.__db = db

    def find_by_id(
        self,
        item_treino_id: uuid.UUID
    ) -> Optional[ItemTreino]:
        return self.__db.get(ItemTreino, item_treino_id)

    def find_by_ficha_treino_id(
        self,
        ficha_treino_id: uuid.UUID
    ) -> list[ItemTreino]:
        return self.__db.query(ItemTreino).filter(
            ItemTreino.ficha_treino_id == ficha_treino_id
        ).all()

    def create(self, item_treino: ItemTreino) -> ItemTreino:
        self.__db.add(item_treino)
        self.__db.commit()
        self.__db.refresh(item_treino)

        return item_treino

    def update(self, item_treino: ItemTreino) -> ItemTreino:
        self.__db.commit()
        self.__db.refresh(item_treino)

        return item_treino

    def delete(self, item_treino: ItemTreino) -> None:
        self.__db.delete(item_treino)
        self.__db.commit()