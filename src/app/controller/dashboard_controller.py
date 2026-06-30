from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, selectinload

from app.config.database import get_db
from app.domain.administrador import Administrador
from app.domain.aluno import Aluno
from app.domain.check_in import CheckIn
from app.domain.exercicio import Exercicio
from app.domain.ficha_treino import FichaTreino
from app.domain.instrutor import Instrutor
from app.domain.item_treino import ItemTreino
from app.domain.matricula import Matricula


router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


def _serialize_check_in(check_in: CheckIn) -> dict:
    return {
        "id": str(check_in.id),
        "aluno_id": str(check_in.aluno_id),
        "data_hora": check_in.data_hora.isoformat(),
    }


def _serialize_matricula(matricula: Matricula) -> dict:
    return {
        "id": str(matricula.id),
        "data_inicio": matricula.data_inicio.isoformat(),
        "ativo": matricula.ativo,
    }


def _serialize_administrador(administrador: Administrador) -> dict:
    return {
        "id": str(administrador.id),
        "nome": administrador.nome,
        "email": administrador.email,
    }


def _serialize_instrutor(instrutor: Instrutor) -> dict:
    return {
        "id": str(instrutor.id),
        "nome": instrutor.nome,
        "email": instrutor.email,
        "cref": instrutor.cref,
    }


def _serialize_exercicio(exercicio: Exercicio) -> dict:
    return {
        "id": str(exercicio.id),
        "nome": exercicio.nome,
        "descricao": exercicio.descricao,
    }


def _serialize_item_treino(item_treino: ItemTreino) -> dict:
    return {
        "id": str(item_treino.id),
        "series": item_treino.series,
        "repeticoes": item_treino.repeticoes,
        "observacao": item_treino.observacao,
        "exercicio": _serialize_exercicio(item_treino.exercicio),
    }


def _serialize_ficha_treino(ficha_treino: FichaTreino) -> dict:
    return {
        "id": str(ficha_treino.id),
        "objetivo": ficha_treino.objetivo,
        "aluno": {
            "id": str(ficha_treino.aluno.id),
            "nome": ficha_treino.aluno.nome,
            "email": ficha_treino.aluno.email,
        },
        "instrutor": {
            "id": str(ficha_treino.instrutor.id),
            "nome": ficha_treino.instrutor.nome,
            "email": ficha_treino.instrutor.email,
            "cref": ficha_treino.instrutor.cref,
        },
        "itens_treino": [
            _serialize_item_treino(item_treino)
            for item_treino in ficha_treino.itens_treino
        ],
    }


def _serialize_aluno(aluno: Aluno, checkins_por_aluno: dict) -> dict:
    return {
        "id": str(aluno.id),
        "nome": aluno.nome,
        "email": aluno.email,
        "cpf": aluno.cpf,
        "telefone": aluno.telefone,
        "matriculas": [
            _serialize_matricula(matricula)
            for matricula in aluno.matriculas
        ],
        "checkins": [
            _serialize_check_in(check_in)
            for check_in in checkins_por_aluno.get(aluno.id, [])
        ],
        "fichas_treino": [
            _serialize_ficha_treino(ficha_treino)
            for ficha_treino in aluno.fichas_treino
        ],
    }


@router.get("/resumo")
def read_resumo(db: Session = Depends(get_db)):
    alunos = (
        db.query(Aluno)
        .options(
            selectinload(Aluno.matriculas),
            selectinload(Aluno.fichas_treino)
            .selectinload(FichaTreino.instrutor),
            selectinload(Aluno.fichas_treino)
            .selectinload(FichaTreino.itens_treino)
            .selectinload(ItemTreino.exercicio),
        )
        .order_by(Aluno.nome)
        .all()
    )

    fichas_treino = (
        db.query(FichaTreino)
        .options(
            selectinload(FichaTreino.aluno),
            selectinload(FichaTreino.instrutor),
            selectinload(FichaTreino.itens_treino)
            .selectinload(ItemTreino.exercicio),
        )
        .order_by(FichaTreino.objetivo)
        .all()
    )

    checkins = db.query(CheckIn).order_by(CheckIn.data_hora.desc()).all()
    checkins_por_aluno: dict = {}

    for checkin in checkins:
        checkins_por_aluno.setdefault(checkin.aluno_id, []).append(checkin)

    return {
        "alunos": [
            _serialize_aluno(aluno, checkins_por_aluno)
            for aluno in alunos
        ]
    }