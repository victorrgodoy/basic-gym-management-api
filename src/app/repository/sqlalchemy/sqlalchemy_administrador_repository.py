import uuid
from typing import Optional
from sqlalchemy.orm import Session
from app.domain.administrador import Administrador
from app.repository.administrador_repository import AdministradorRepository

class SqlAlchemyAdministradorRepository(AdministradorRepository):    
    def __init__(self, db: Session):
        self.__db = db

    def find_by_id(self, id: uuid.UUID) -> Optional[Administrador]:
        return self.__db.query(Administrador).filter(Administrador.id == id).first()

    def create(self, administrador: Administrador) -> Administrador:
        self.__db.add(administrador)
        self.__db.commit()
        self.__db.refresh(administrador)
        return administrador
    
    def read(self) -> list[Administrador]:
        return self.__db.query(Administrador).all()