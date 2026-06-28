from fastapi import FastAPI

from app.routers.aluno_router import router as aluno_router

app = FastAPI(title="Basic Gym Management API")

app.include_router(aluno_router)