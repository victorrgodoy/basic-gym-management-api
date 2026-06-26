# import uuid

# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session

# from app.config.database import get_db
# from app.domains.aluno import Aluno
# from app.repositories.aluno_repository import AlunoRepository
# from app.schemas.aluno_schema import AlunoRequest, AlunoResponse
# from app.services.aluno_service import AlunoService

# router = APIRouter(prefix="/alunos", tags=["Alunos"])


# def get_service(db: Session = Depends(get_db)) -> AlunoService:
#     repository = AlunoRepository(db)
#     return AlunoService(repository)

# @router.get("/{id}", response_model=AlunoResponse)
# def find_by_id(id: uuid.UUID, service: AlunoService = Depends(get_service)):
#     aluno = service.find_by_id(id)
#     if not aluno:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado.")
#     return aluno

# @router.post("/", response_model=AlunoResponse, status_code=status.HTTP_201_CREATED)
# def create(request: AlunoRequest, service: AlunoService = Depends(get_service)):
#     aluno = Aluno(nome=request.nome, email=request.email, cpf=request.cpf)
#     return service.create(aluno)

# @router.get("/", response_model=list[AlunoResponse])
# def list_all(service: AlunoService = Depends(get_service)):
#     return service.list_all()

# @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete(id: uuid.UUID, service: AlunoService = Depends(get_service)):
#     service.delete(id)