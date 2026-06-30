import uuid

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.domain.item_treino import ItemTreino
from app.repository.sqlalchemy.sqlalchemy_exercicio_repository import (
    SqlAlchemyExercicioRepository
)
from app.repository.sqlalchemy.sqlalchemy_ficha_treino_repository import (
    SqlAlchemyFichaTreinoRepository
)
from app.repository.sqlalchemy.sqlalchemy_item_treino_repository import (
    SqlAlchemyItemTreinoRepository
)
from app.request.item_treino_request import (
    ItemTreinoCreateRequest,
    ItemTreinoResponse,
    ItemTreinoUpdateRequest
)
from app.service.item_treino_service import ItemTreinoService


router = APIRouter(tags=["Itens de Treino"])


def get_item_treino_service(
    db: Session = Depends(get_db)
) -> ItemTreinoService:
    return ItemTreinoService(
        item_treino_repository=SqlAlchemyItemTreinoRepository(db),
        ficha_treino_repository=SqlAlchemyFichaTreinoRepository(db),
        exercicio_repository=SqlAlchemyExercicioRepository(db)
    )


@router.post(
    "/fichas-treino/{ficha_treino_id}/itens/",
    response_model=ItemTreinoResponse,
    status_code=status.HTTP_201_CREATED
)
def create(
    ficha_treino_id: uuid.UUID,
    request: ItemTreinoCreateRequest,
    service: ItemTreinoService = Depends(get_item_treino_service)
):
    try:
        item_treino = ItemTreino(
            ficha_treino_id=ficha_treino_id,
            exercicio_id=request.exercicio_id,
            series=request.series,
            repeticoes=request.repeticoes,
            observacao=request.observacao
        )

        return service.create(item_treino)

    except LookupError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error)
        ) from error


@router.get(
    "/fichas-treino/{ficha_treino_id}/itens/",
    response_model=list[ItemTreinoResponse]
)
def read_by_ficha_treino(
    ficha_treino_id: uuid.UUID,
    service: ItemTreinoService = Depends(get_item_treino_service)
):
    try:
        return service.read_by_ficha_treino(ficha_treino_id)

    except LookupError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error)
        ) from error


@router.get(
    "/itens-treino/{item_treino_id}",
    response_model=ItemTreinoResponse
)
def find_by_id(
    item_treino_id: uuid.UUID,
    service: ItemTreinoService = Depends(get_item_treino_service)
):
    item_treino = service.find_by_id(item_treino_id)

    if not item_treino:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item de treino não encontrado."
        )

    return item_treino


@router.put(
    "/itens-treino/{item_treino_id}",
    response_model=ItemTreinoResponse
)
def update(
    item_treino_id: uuid.UUID,
    request: ItemTreinoUpdateRequest,
    service: ItemTreinoService = Depends(get_item_treino_service)
):
    try:
        return service.update(
            item_treino_id=item_treino_id,
            exercicio_id=request.exercicio_id,
            series=request.series,
            repeticoes=request.repeticoes,
            observacao=request.observacao,
            atualizar_observacao=(
                "observacao" in request.model_fields_set
            )
        )

    except LookupError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error)
        ) from error

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error


@router.delete(
    "/itens-treino/{item_treino_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete(
    item_treino_id: uuid.UUID,
    service: ItemTreinoService = Depends(get_item_treino_service)
):
    try:
        service.delete(item_treino_id)

        return Response(status_code=status.HTTP_204_NO_CONTENT)

    except LookupError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error)
        ) from error