import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db 
from app.repository.sqlalchemy.sqlalchemy_usuario_repository import SqlAlchemyUsuarioRepository
from app.service.usuario_service import UsuarioService
from app.repository.sqlalchemy.sqlalchemy_aluno_repository import SqlAlchemyAlunoRepository
from app.service.aluno_service import AlunoService
from app.domain.aluno import Aluno
from app.request.aluno_request import AlunoCreateRequest, AlunoUpdateRequest

router = APIRouter(prefix="/alunos", tags=["Alunos"])

def get_aluno_service(db: Session = Depends(get_db)):
    return AlunoService(
        SqlAlchemyAlunoRepository(db),
        UsuarioService(SqlAlchemyUsuarioRepository(db))
    )

@router.post("/", status_code=201)
def create(request: AlunoCreateRequest, service: AlunoService = Depends(get_aluno_service)):
    try:
        novo_aluno = Aluno(
            nome=request.nome,
            email=request.email,
            senha=request.senha,
            cpf=request.cpf,
            telefone=request.telefone
        )
        return service.create(novo_aluno)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
def read(service: AlunoService = Depends(get_aluno_service)):
    return service.read()

@router.put("/{aluno_id}")
def update(aluno_id: uuid.UUID, request: AlunoUpdateRequest, service: AlunoService = Depends(get_aluno_service)):
    try:
        return service.update(aluno_id, request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{aluno_id}")
def delete(aluno_id: uuid.UUID, service: AlunoService = Depends(get_aluno_service)):
    try:
        service.delete(aluno_id)
        return {"message": "Aluno deletado com sucesso."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))