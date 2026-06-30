import uuid
from typing import Optional
from sqlalchemy.orm import Session
from app.domain.aluno import Aluno
from app.repository.aluno_repository import AlunoRepository

class SqlAlchemyAlunoRepository(AlunoRepository):    
    def __init__(self, db: Session):
        self.__db = db

    def find_by_id(self, id: uuid.UUID) -> Optional[Aluno]:
        return self.__db.query(Aluno).filter(Aluno.id == id).first()
    
    def find_by_cpf(self, cpf: str) -> Optional[Aluno]: 
        return self.__db.query(Aluno).filter(Aluno.cpf == cpf).first()

    def create(self, aluno: Aluno) -> Aluno:
        self.__db.add(aluno)
        self.__db.commit()
        self.__db.refresh(aluno)
        return aluno
    
    def read(self) -> list[Aluno]:
        return self.__db.query(Aluno).all()