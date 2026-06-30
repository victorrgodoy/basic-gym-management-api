import uuid

from typing import Optional

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.domain.ficha_treino import FichaTreino
from app.repository.ficha_treino_repository import FichaTreinoRepository


class SqlAlchemyFichaTreinoRepository(FichaTreinoRepository):

    def __init__(self, db: Session):
        self.__db = db

    def find_by_id(
        self,
        ficha_treino_id: uuid.UUID
    ) -> Optional[FichaTreino]:
        return self.__db.get(FichaTreino, ficha_treino_id)

    def create(self, ficha_treino: FichaTreino) -> FichaTreino:
        self.__db.add(ficha_treino)
        self.__db.commit()
        self.__db.refresh(ficha_treino)

        return ficha_treino

    def read(self) -> list[FichaTreino]:
        return self.__db.query(FichaTreino).order_by(
            FichaTreino.objetivo
        ).all()

    def update(self, ficha_treino: FichaTreino) -> FichaTreino:
        self.__db.commit()
        self.__db.refresh(ficha_treino)

        return ficha_treino

    def delete(self, ficha_treino: FichaTreino) -> None:
        try:
            self.__db.delete(ficha_treino)
            self.__db.commit()

        except IntegrityError as error:
            self.__db.rollback()

            raise ValueError(
                "Não foi possível excluir a ficha de treino."
            ) from error