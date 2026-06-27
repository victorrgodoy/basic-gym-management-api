from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.domain.instrutor import Instrutor
from app.request.instrutor_request import InstrutorRequest
from app.service.instrutor_service import InstrutorService
from app.service.usuario_service import UsuarioService
from app.repository.sqlalchemy.sqlalchemy_instrutor_repository import SqlAlchemyInstrutorRepository
from app.repository.sqlalchemy.sqlalchemy_usuario_repository import SqlAlchemyUsuarioRepository

router = APIRouter(prefix="/instrutores", tags=["Instrutores"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def criar_instrutor(request: InstrutorRequest, db: Session = Depends(get_db)):
    try:
        instrutor_repo = SqlAlchemyInstrutorRepository(db)
        usuario_repo = SqlAlchemyUsuarioRepository(db)
        
        usuario_service = UsuarioService(usuario_repo)
        service = InstrutorService(instrutor_repo, usuario_service)
        
        novo_instrutor = Instrutor(
            nome=request.nome,
            email=request.email,
            senha=request.senha,
            cref=request.cref
        )
        
        return service.create(novo_instrutor)
        
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=str(e)
        )


@router.get("/")
def listar_instrutores(db: Session = Depends(get_db)):
    instrutor_repo = SqlAlchemyInstrutorRepository(db)
    usuario_repo = SqlAlchemyUsuarioRepository(db)
    usuario_service = UsuarioService(usuario_repo)
    
    service = InstrutorService(instrutor_repo, usuario_service)
    return service.read()