import uuid

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.domain.ficha_treino import FichaTreino
from app.repository.sqlalchemy.sqlalchemy_aluno_repository import (
    SqlAlchemyAlunoRepository
)
from app.repository.sqlalchemy.sqlalchemy_ficha_treino_repository import (
    SqlAlchemyFichaTreinoRepository
)
from app.repository.sqlalchemy.sqlalchemy_instrutor_repository import (
    SqlAlchemyInstrutorRepository
)
from app.request.ficha_treino_request import (
    FichaTreinoCreateRequest,
    FichaTreinoResponse,
    FichaTreinoUpdateRequest
)
from app.service.ficha_treino_service import FichaTreinoService


router = APIRouter(
    prefix="/fichas-treino",
    tags=["Fichas de Treino"]
)


def get_ficha_treino_service(
    db: Session = Depends(get_db)
) -> FichaTreinoService:
    return FichaTreinoService(
        ficha_treino_repository=SqlAlchemyFichaTreinoRepository(db),
        aluno_repository=SqlAlchemyAlunoRepository(db),
        instrutor_repository=SqlAlchemyInstrutorRepository(db)
    )


@router.post(
    "/",
    response_model=FichaTreinoResponse,
    status_code=status.HTTP_201_CREATED
)
def create(
    request: FichaTreinoCreateRequest,
    service: FichaTreinoService = Depends(get_ficha_treino_service)
):
    try:
        ficha_treino = FichaTreino(
            objetivo=request.objetivo,
            aluno_id=request.aluno_id,
            instrutor_id=request.instrutor_id
        )

        return service.create(ficha_treino)

    except LookupError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error)
        ) from error


@router.get(
    "/",
    response_model=list[FichaTreinoResponse]
)
def read(
    service: FichaTreinoService = Depends(get_ficha_treino_service)
):
    return service.read()


@router.get(
    "/{ficha_treino_id}",
    response_model=FichaTreinoResponse
)
def find_by_id(
    ficha_treino_id: uuid.UUID,
    service: FichaTreinoService = Depends(get_ficha_treino_service)
):
    ficha_treino = service.find_by_id(ficha_treino_id)

    if not ficha_treino:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ficha de treino não encontrada."
        )

    return ficha_treino


@router.put(
    "/{ficha_treino_id}",
    response_model=FichaTreinoResponse
)
def update(
    ficha_treino_id: uuid.UUID,
    request: FichaTreinoUpdateRequest,
    service: FichaTreinoService = Depends(get_ficha_treino_service)
):
    try:
        return service.update(
            ficha_treino_id=ficha_treino_id,
            objetivo=request.objetivo,
            aluno_id=request.aluno_id,
            instrutor_id=request.instrutor_id
        )

    except LookupError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error)
        ) from error


@router.delete(
    "/{ficha_treino_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete(
    ficha_treino_id: uuid.UUID,
    service: FichaTreinoService = Depends(get_ficha_treino_service)
):
    try:
        service.delete(ficha_treino_id)

        return Response(status_code=status.HTTP_204_NO_CONTENT)

    except LookupError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error)
        ) from error

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error)
        ) from error