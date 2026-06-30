import uuid

from typing import Optional

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.domain.exercicio import Exercicio
from app.repository.exercicio_repository import ExercicioRepository


class SqlAlchemyExercicioRepository(ExercicioRepository):

    def __init__(self, db: Session):
        self.__db = db

    def find_by_id(
        self,
        exercicio_id: uuid.UUID
    ) -> Optional[Exercicio]:
        return self.__db.get(Exercicio, exercicio_id)

    def find_by_nome(self, nome: str) -> Optional[Exercicio]:
        return self.__db.query(Exercicio).filter(
            Exercicio.nome == nome
        ).first()

    def create(self, exercicio: Exercicio) -> Exercicio:
        self.__db.add(exercicio)
        self.__db.commit()
        self.__db.refresh(exercicio)

        return exercicio

    def read(self) -> list[Exercicio]:
        return self.__db.query(Exercicio).order_by(
            Exercicio.nome
        ).all()

    def update(self, exercicio: Exercicio) -> Exercicio:
        self.__db.commit()
        self.__db.refresh(exercicio)

        return exercicio

    def delete(self, exercicio: Exercicio) -> None:
        try:
            self.__db.delete(exercicio)
            self.__db.commit()

        except IntegrityError as error:
            self.__db.rollback()

            raise ValueError(
                "Não é possível excluir este exercício porque ele está "
                "vinculado a um item de treino."
            ) from error