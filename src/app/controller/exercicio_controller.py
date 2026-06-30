import uuid

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.domain.exercicio import Exercicio
from app.repository.sqlalchemy.sqlalchemy_exercicio_repository import (
    SqlAlchemyExercicioRepository
)
from app.request.exercicio_request import (
    ExercicioCreateRequest,
    ExercicioResponse,
    ExercicioUpdateRequest
)
from app.service.exercicio_service import ExercicioService


router = APIRouter(
    prefix="/exercicios",
    tags=["Exercícios"]
)


def get_exercicio_service(
    db: Session = Depends(get_db)
) -> ExercicioService:
    repository = SqlAlchemyExercicioRepository(db)

    return ExercicioService(repository)


@router.post(
    "/",
    response_model=ExercicioResponse,
    status_code=status.HTTP_201_CREATED
)
def create(
    request: ExercicioCreateRequest,
    service: ExercicioService = Depends(get_exercicio_service)
):
    try:
        exercicio = Exercicio(
            nome=request.nome,
            descricao=request.descricao
        )

        return service.create(exercicio)

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error)
        ) from error


@router.get(
    "/",
    response_model=list[ExercicioResponse]
)
def read(
    service: ExercicioService = Depends(get_exercicio_service)
):
    return service.read()


@router.get(
    "/{exercicio_id}",
    response_model=ExercicioResponse
)
def find_by_id(
    exercicio_id: uuid.UUID,
    service: ExercicioService = Depends(get_exercicio_service)
):
    exercicio = service.find_by_id(exercicio_id)

    if not exercicio:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exercício não encontrado."
        )

    return exercicio


@router.put(
    "/{exercicio_id}",
    response_model=ExercicioResponse
)
def update(
    exercicio_id: uuid.UUID,
    request: ExercicioUpdateRequest,
    service: ExercicioService = Depends(get_exercicio_service)
):
    try:
        return service.update(
            exercicio_id=exercicio_id,
            nome=request.nome,
            descricao=request.descricao
        )

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


@router.delete(
    "/{exercicio_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete(
    exercicio_id: uuid.UUID,
    service: ExercicioService = Depends(get_exercicio_service)
):
    try:
        service.delete(exercicio_id)

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