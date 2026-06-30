from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.domain.administrador import Administrador
from app.request.administrador_request import AdministradorRequest
from app.service.usuario_service import UsuarioService
from app.service.administrador_service import AdministradorService
from app.repository.sqlalchemy.sqlalchemy_usuario_repository import SqlAlchemyUsuarioRepository
from app.repository.sqlalchemy.sqlalchemy_administrador_repository import SqlAlchemyAdministradorRepository
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from app.request.administrador_request import AdministradorUpdate

router = APIRouter(prefix="/administradores", tags=["Administradores"])

def get_administrador_service(db: Session = Depends(get_db)):
    return AdministradorService(
        SqlAlchemyAdministradorRepository(db),
        UsuarioService(SqlAlchemyUsuarioRepository(db))
    )

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: AdministradorRequest, service: AdministradorService = Depends(get_administrador_service)):
    try:
        novo_admin = Administrador(
            nome=request.nome,
            email=request.email,
            senha=request.senha
        )
        
        return service.create(novo_admin)
        
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=str(e)
        )


@router.get("/")
def read(service: AdministradorService = Depends(get_administrador_service)):
    return service.read()

@router.put("/{id}", response_model=None)
def update(id: UUID, dados: AdministradorUpdate, service: AdministradorService = Depends(get_administrador_service)):
    try:
        return service.update(id, dados)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: UUID, service: AdministradorService = Depends(get_administrador_service)):
    try:
        service.delete(id)
        return
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))