import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.repository.sqlalchemy.sqlalchemy_usuario_repository import SqlAlchemyUsuarioRepository
from app.service.usuario_service import UsuarioService
from app.repository.sqlalchemy.sqlalchemy_instrutor_repository import SqlAlchemyInstrutorRepository
from app.service.instrutor_service import InstrutorService
from app.domain.instrutor import Instrutor
from app.request.instrutor_request import InstrutorCreateRequest, InstrutorUpdateRequest

router = APIRouter(prefix="/instrutores", tags=["Instrutores"])

def get_instrutor_service(db: Session = Depends(get_db)):
    return InstrutorService(
        SqlAlchemyInstrutorRepository(db),
        UsuarioService(SqlAlchemyUsuarioRepository(db))
    )

@router.post("/", status_code=201)
def create(request: InstrutorCreateRequest, service: InstrutorService = Depends(get_instrutor_service)):
    try:
        novo_instrutor = Instrutor(
            nome=request.nome,
            email=request.email,
            senha=request.senha,
            cref=request.cref
        )
        return service.create(novo_instrutor)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
def read(service: InstrutorService = Depends(get_instrutor_service)):
    return service.read()

@router.put("/{instrutor_id}")
def update(instrutor_id: uuid.UUID, request: InstrutorUpdateRequest, service: InstrutorService = Depends(get_instrutor_service)):
    try:
        return service.update(instrutor_id, request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{instrutor_id}")
def delete(instrutor_id: uuid.UUID, service: InstrutorService = Depends(get_instrutor_service)):
    try:
        service.delete(instrutor_id)
        return {"message": "Instrutor deletado com sucesso."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))