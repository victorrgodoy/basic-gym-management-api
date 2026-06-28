from sqlalchemy.orm import Session
from app.domain.aluno import Aluno
import uuid
from typing import Optional
 
class AlunoRepository:
    def __init__(self, db: Session):
        self.__db = db
    
    def find_by_id(self, id: uuid.UUID) -> Optional[Aluno]:
        return self.__db.query(Aluno).filter(Aluno.id == id).first()
    
    def create(self, aluno: Aluno) -> Aluno:
        self.__db.add(aluno)
        self.__db.commit()
        self.__db.refresh(aluno)
        return aluno
    
    def list_all(self) -> list[Aluno]:
        return self.__db.query(Aluno).all()
    
    def delete(self, id: uuid.UUID) -> None:
        aluno = self.__db.query(Aluno).filter(Aluno.id == id).first()
        self.__db.delete(aluno)
        self.__db.commit()
            
   




