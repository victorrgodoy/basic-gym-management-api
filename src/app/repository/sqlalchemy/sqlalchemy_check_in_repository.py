import uuid
from typing import List
from sqlalchemy.orm import Session
from app.domain.check_in import CheckIn

class SqlAlchemyCheckInRepository:
    def __init__(self, db: Session):
        self.__db = db

    def create(self, check_in: CheckIn) -> CheckIn:
        self.__db.add(check_in)
        self.__db.commit()
        self.__db.refresh(check_in)
        return check_in

    def find_by_aluno_id(self, aluno_id: uuid.UUID) -> List[CheckIn]:
        return self.__db.query(CheckIn).filter(CheckIn.aluno_id == aluno_id).order_by(CheckIn.data_hora.desc()).all()

    def read(self) -> List[CheckIn]:
        return self.__db.query(CheckIn).order_by(CheckIn.data_hora.desc()).all()