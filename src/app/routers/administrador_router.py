from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.domain.administrador import Administrador
from app.request.administrador_request import AdministradorRequest
from app.service.usuario_service import UsuarioService
from app.repository.sqlalchemy.sqlalchemy_usuario_repository import SqlAlchemyUsuarioRepository

router = APIRouter(prefix="/administradores", tags=["Administradores"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def criar_administrador(request: AdministradorRequest, db: Session = Depends(get_db)):
    try:
        usuario_repo = SqlAlchemyUsuarioRepository(db)
        service = UsuarioService(usuario_repo)
        
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
def listar_administradores(db: Session = Depends(get_db)):
    usuario_repo = SqlAlchemyUsuarioRepository(db)
    service = UsuarioService(usuario_repo)
    return service.read(tipo="administrador")