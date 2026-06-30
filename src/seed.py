from __future__ import annotations

from datetime import date, datetime
from uuid import UUID

from app.config.database import SessionLocal
from app.domain.administrador import Administrador
from app.domain.aluno import Aluno
from app.domain.check_in import CheckIn
from app.domain.exercicio import Exercicio
from app.domain.ficha_treino import FichaTreino
from app.domain.instrutor import Instrutor
from app.domain.item_treino import ItemTreino
from app.domain.matricula import Matricula
from app.domain.usuario import Usuario


ADMINISTRADOR_ID = UUID("11111111-1111-1111-1111-111111111111")
INSTRUTOR_ID = UUID("22222222-2222-2222-2222-222222222222")
ALUNO_ANA_ID = UUID("33333333-3333-3333-3333-333333333333")
ALUNO_BRUNO_ID = UUID("44444444-4444-4444-4444-444444444444")

EXERCICIO_SUPINO_ID = UUID("55555555-5555-5555-5555-555555555555")
EXERCICIO_AGACHAMENTO_ID = UUID("66666666-6666-6666-6666-666666666666")
EXERCICIO_REMO_ID = UUID("77777777-7777-7777-7777-777777777777")
EXERCICIO_PUXADA_ID = UUID("88888888-8888-8888-8888-888888888888")

FICHA_ANA_ID = UUID("99999999-9999-9999-9999-999999999999")
FICHA_BRUNO_ID = UUID("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa")

ITEM_ANA_1_ID = UUID("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb")
ITEM_ANA_2_ID = UUID("cccccccc-cccc-cccc-cccc-cccccccccccc")
ITEM_BRUNO_1_ID = UUID("dddddddd-dddd-dddd-dddd-dddddddddddd")
ITEM_BRUNO_2_ID = UUID("eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee")

MATRICULA_ANA_ID = UUID("ffffffff-ffff-ffff-ffff-ffffffffffff")
MATRICULA_BRUNO_ID = UUID("12345678-1234-1234-1234-123456789012")

CHECKIN_ANA_ID = UUID("23456789-2345-2345-2345-234567890123")
CHECKIN_BRUNO_ID = UUID("34567890-3456-3456-3456-345678901234")


def ensure_entity(db, model, entity_id, factory):
    existing = db.get(model, entity_id)

    if existing is not None:
        return existing

    entity = factory()
    db.add(entity)
    return entity


def clear_database(db) -> None:
    db.query(CheckIn).delete(synchronize_session=False)
    db.query(ItemTreino).delete(synchronize_session=False)
    db.query(FichaTreino).delete(synchronize_session=False)
    db.query(Matricula).delete(synchronize_session=False)
    db.query(Aluno).delete(synchronize_session=False)
    db.query(Instrutor).delete(synchronize_session=False)
    db.query(Administrador).delete(synchronize_session=False)
    db.query(Exercicio).delete(synchronize_session=False)
    db.query(Usuario).delete(synchronize_session=False)
    db.query(Instrutor).delete(synchronize_session=False)
    db.query(Aluno).delete(synchronize_session=False)
    db.query(Exercicio).delete(synchronize_session=False)
    db.query(Usuario).delete(synchronize_session=False)


def seed_database() -> None:
    db = SessionLocal()

    try:
        clear_database(db)

        administrador = ensure_entity(
            db,
            Administrador,
            ADMINISTRADOR_ID,
            lambda: Administrador(
                id=ADMINISTRADOR_ID,
                nome="Mariana Rocha",
                email="mariana.rocha@basicgym.com",
                senha="admin123",
            ),
        )

        instrutor = ensure_entity(
            db,
            Instrutor,
            INSTRUTOR_ID,
            lambda: Instrutor(
                id=INSTRUTOR_ID,
                nome="Lucas Ferreira",
                email="lucas.ferreira@basicgym.com",
                senha="instrutor123",
                cref="123456-7",
            ),
        )

        aluno_ana = ensure_entity(
            db,
            Aluno,
            ALUNO_ANA_ID,
            lambda: Aluno(
                id=ALUNO_ANA_ID,
                nome="José Santos",
                email="jose.santos@basicgym.com",
                senha="aluno123",
                cpf="123.456.789-01",
                telefone="(12) 99123-4567",
            ),
        )

        aluno_bruno = ensure_entity(
            db,
            Aluno,
            ALUNO_BRUNO_ID,
            lambda: Aluno(
                id=ALUNO_BRUNO_ID,
                nome="Bruno Almeida",
                email="bruno.almeida@basicgym.com",
                senha="aluno123",
                cpf="987.654.321-09",
                telefone="(12) 99876-5432",
            ),
        )

        exercicio_supino = ensure_entity(
            db,
            Exercicio,
            EXERCICIO_SUPINO_ID,
            lambda: Exercicio(
                id=EXERCICIO_SUPINO_ID,
                nome="Supino inclinado com halteres",
                descricao="Série para peitoral superior, com controle de amplitude e estabilização dos ombros.",
            ),
        )

        exercicio_agachamento = ensure_entity(
            db,
            Exercicio,
            EXERCICIO_AGACHAMENTO_ID,
            lambda: Exercicio(
                id=EXERCICIO_AGACHAMENTO_ID,
                nome="Agachamento livre com barra",
                descricao="Execução para membros inferiores, priorizando postura, profundidade e core ativo.",
            ),
        )

        exercicio_remo = ensure_entity(
            db,
            Exercicio,
            EXERCICIO_REMO_ID,
            lambda: Exercicio(
                id=EXERCICIO_REMO_ID,
                nome="Remada baixa no cabo",
                descricao="Puxada horizontal para dorsais, romboides e posterior de ombro.",
            ),
        )

        exercicio_puxada = ensure_entity(
            db,
            Exercicio,
            EXERCICIO_PUXADA_ID,
            lambda: Exercicio(
                id=EXERCICIO_PUXADA_ID,
                nome="Puxada alta aberta",
                descricao="Puxada vertical para dorsais e bíceps, com atenção ao controle da volta.",
            ),
        )

        ficha_ana = ensure_entity(
            db,
            FichaTreino,
            FICHA_ANA_ID,
            lambda: FichaTreino(
                id=FICHA_ANA_ID,
                objetivo="Hipertrofia de membros superiores e postura",
                aluno_id=aluno_ana.id,
                instrutor_id=instrutor.id,
            ),
        )

        ficha_bruno = ensure_entity(
            db,
            FichaTreino,
            FICHA_BRUNO_ID,
            lambda: FichaTreino(
                id=FICHA_BRUNO_ID,
                objetivo="Condicionamento físico geral e ganho de força",
                aluno_id=aluno_bruno.id,
                instrutor_id=instrutor.id,
            ),
        )

        ensure_entity(
            db,
            Matricula,
            MATRICULA_ANA_ID,
            lambda: Matricula(
                id=MATRICULA_ANA_ID,
                data_inicio=date(2026, 3, 4),
                ativo=True,
                aluno_id=aluno_ana.id,
            ),
        )

        ensure_entity(
            db,
            Matricula,
            MATRICULA_BRUNO_ID,
            lambda: Matricula(
                id=MATRICULA_BRUNO_ID,
                data_inicio=date(2026, 4, 18),
                ativo=True,
                aluno_id=aluno_bruno.id,
            ),
        )

        ensure_entity(
            db,
            ItemTreino,
            ITEM_ANA_1_ID,
            lambda: ItemTreino(
                id=ITEM_ANA_1_ID,
                ficha_treino_id=ficha_ana.id,
                exercicio_id=exercicio_supino.id,
                series=4,
                repeticoes=10,
                observacao="Manter 90 segundos de descanso entre as séries e subir a carga apenas se completar todas as repetições com técnica.",
            ),
        )

        ensure_entity(
            db,
            ItemTreino,
            ITEM_ANA_2_ID,
            lambda: ItemTreino(
                id=ITEM_ANA_2_ID,
                ficha_treino_id=ficha_ana.id,
                exercicio_id=exercicio_remo.id,
                series=4,
                repeticoes=12,
                observacao="Segurar 1 segundo na contração máxima e evitar jogar o tronco para trás.",
            ),
        )

        ensure_entity(
            db,
            ItemTreino,
            ITEM_BRUNO_1_ID,
            lambda: ItemTreino(
                id=ITEM_BRUNO_1_ID,
                ficha_treino_id=ficha_bruno.id,
                exercicio_id=exercicio_agachamento.id,
                series=5,
                repeticoes=8,
                observacao="Fazer aquecimento de quadril antes da série principal e manter a coluna neutra durante toda a execução.",
            ),
        )

        ensure_entity(
            db,
            ItemTreino,
            ITEM_BRUNO_2_ID,
            lambda: ItemTreino(
                id=ITEM_BRUNO_2_ID,
                ficha_treino_id=ficha_bruno.id,
                exercicio_id=exercicio_puxada.id,
                series=4,
                repeticoes=10,
                observacao="Puxar até a linha do peito sem usar impulso e controlar a fase excêntrica.",
            ),
        )

        ensure_entity(
            db,
            CheckIn,
            CHECKIN_ANA_ID,
            lambda: CheckIn(
                aluno_id=aluno_ana.id,
                data_hora=datetime(2026, 6, 30, 7, 12),
            ),
        )

        ensure_entity(
            db,
            CheckIn,
            CHECKIN_BRUNO_ID,
            lambda: CheckIn(
                aluno_id=aluno_bruno.id,
                data_hora=datetime(2026, 6, 30, 18, 36),
            ),
        )

        db.commit()

        print("Seed concluído com sucesso.")
        print(f"Administrador: {administrador.email}")
        print(f"Instrutor: {instrutor.email}")
        print(f"Alunos: {aluno_ana.email}, {aluno_bruno.email}")
        print(f"Fichas: {ficha_ana.id}, {ficha_bruno.id}")

    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()