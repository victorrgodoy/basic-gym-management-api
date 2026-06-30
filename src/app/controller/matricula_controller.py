import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.repository.sqlalchemy.sqlalchemy_matricula_repository import SqlAlchemyMatriculaRepository
from app.service.matricula_service import MatriculaService
from app.domain.matricula import Matricula
from datetime import date

router = APIRouter(prefix="/matriculas", tags=["Matriculas"])

def get_matricula_service(db: Session = Depends(get_db)):
    return MatriculaService(
        SqlAlchemyMatriculaRepository(db)
    )

@router.post("/{aluno_id}", status_code=201)
def create(
    aluno_id: uuid.UUID, 
    service: MatriculaService = Depends(get_matricula_service)
):
    try:
        nova_matricula = Matricula(
            aluno_id=aluno_id,
            data_inicio=date.today(),
            ativo=True 
        )
        return service.create(nova_matricula)
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
def read(service: MatriculaService = Depends(get_matricula_service)):
    return service.read()

@router.patch("/{matricula_id}/ativar")
def ativar(matricula_id: uuid.UUID, service: MatriculaService = Depends(get_matricula_service)):
    try:
        return service.ativar(matricula_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))    

@router.patch("/{matricula_id}/desativar")
def desativar(matricula_id: uuid.UUID, service: MatriculaService = Depends(get_matricula_service)):
    try:
        return service.desativar(matricula_id) 
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))