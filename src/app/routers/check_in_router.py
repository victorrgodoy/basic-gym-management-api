from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.request.check_in_request import CheckInRequest
from app.service.check_in_service import CheckInService
from app.repository.sqlalchemy.sqlalchemy_check_in_repository import SqlAlchemyCheckInRepository
from app.repository.sqlalchemy.sqlalchemy_usuario_repository import SqlAlchemyUsuarioRepository

router = APIRouter(prefix="/checkins", tags=["CheckIns"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def registrar_check_in(request: CheckInRequest, db: Session = Depends(get_db)):
    try:
        check_in_repo = SqlAlchemyCheckInRepository(db)
        usuario_repo = SqlAlchemyUsuarioRepository(db)
        service = CheckInService(check_in_repo, usuario_repo)
        return service.create(request.aluno_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/")
def listar_check_ins(db: Session = Depends(get_db)):
    check_in_repo = SqlAlchemyCheckInRepository(db)
    usuario_repo = SqlAlchemyUsuarioRepository(db)
    service = CheckInService(check_in_repo, usuario_repo)
    return service.read_all()

@router.get("/aluno/{aluno_id}")
def listar_check_ins_por_aluno(aluno_id: UUID, db: Session = Depends(get_db)):
    check_in_repo = SqlAlchemyCheckInRepository(db)
    usuario_repo = SqlAlchemyUsuarioRepository(db)
    service = CheckInService(check_in_repo, usuario_repo)
    return service.read_by_aluno(aluno_id)