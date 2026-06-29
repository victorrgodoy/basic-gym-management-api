import uuid
from typing import Optional
from sqlalchemy.orm import Session
from app.domain.instrutor import Instrutor
from app.repository.instrutor_repository import InstrutorRepository

class SqlAlchemyInstrutorRepository(InstrutorRepository):    
    def __init__(self, db: Session):
        self.__db = db
    
    def find_by_id(self, id: uuid.UUID) -> Optional[Instrutor]:
        return self.__db.query(Instrutor).filter(Instrutor.id == id).first()

    def find_by_cref(self, cref: str) -> Optional[Instrutor]:
        return self.__db.query(Instrutor).filter(Instrutor.cref == cref).first()    

    def create(self, instrutor: Instrutor) -> Instrutor:
        self.__db.add(instrutor)
        self.__db.commit()
        self.__db.refresh(instrutor)
        return instrutor    
    
    def read(self) -> list[Instrutor]:
        return self.__db.query(Instrutor).all()