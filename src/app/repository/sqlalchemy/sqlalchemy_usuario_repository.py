import uuid
from typing import Optional
from sqlalchemy.orm import Session
from app.repository.usuario_repository import UsuarioRepository
from app.domain.usuario import Usuario 

class SqlAlchemyUsuarioRepository(UsuarioRepository):    
    def __init__(self, db: Session):
        self.__db = db
    
    def find_by_id(self, usuario_id: uuid.UUID) -> Optional[Usuario]: 
        return self.__db.query(Usuario).filter(Usuario.id == usuario_id).first()
        
    def find_by_email(self, email: str) -> Optional[Usuario]:
        return self.__db.query(Usuario).filter(Usuario.email == email).first()
    
    def update(self, usuario: Usuario) -> Usuario:
        usuario_atualizado = self.__db.merge(usuario)
        self.__db.commit()
        self.__db.refresh(usuario_atualizado)
        return usuario_atualizado

    def delete(self, usuario_id: uuid.UUID) -> None: 
        usuario = self.__db.query(Usuario).filter(Usuario.id == usuario_id).first()
        self.__db.delete(usuario)
        self.__db.commit()