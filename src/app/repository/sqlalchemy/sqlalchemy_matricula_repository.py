import uuid
from typing import Optional
from sqlalchemy.orm import Session
from app.domain.matricula import Matricula
from app.repository.matricula_repository import MatriculaRepository

class SqlAlchemyMatriculaRepository(MatriculaRepository):
    def __init__(self, db: Session):
        self.__db = db

    def find_by_id(self, id: uuid.UUID) -> Optional[Matricula]:
        return self.__db.query(Matricula).filter(Matricula.id == id).first()

    def create(self, matricula: Matricula) -> Matricula:
        self.__db.add(matricula)
        self.__db.commit()
        self.__db.refresh(matricula)
        return matricula
    
    def read(self) -> list[Matricula]:
        return self.__db.query(Matricula).all()
    
    def update(self, matricula: Matricula) -> Matricula:
        self.__db.add(matricula) 
        self.__db.commit()
        self.__db.refresh(matricula)
        return matricula