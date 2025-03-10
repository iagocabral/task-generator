from fastapi import FastAPI
from app.core.database import create_tables
from app.api.routes_users import router as user_router
from app.api.routes_tasks import router as task_router
from app.api.routes_auth import router as auth_router
from app.api.routes_ai import router as ai_router

app = FastAPI(
    title="SaaS - Gerador Automático de Tarefas",
    description="API para um sistema SaaS que gera e gerencia tarefas automaticamente.",
    version="1.0.0",
    contact={
        "name": "Seu Nome",
        "email": "seuemail@email.com",
    },
)

# Criar tabelas no banco de dados
create_tables()

# Incluir as rotas no FastAPI
app.include_router(user_router, tags=["Usuários"])
app.include_router(task_router, tags=["Tarefas"])
app.include_router(auth_router, tags=["Autenticação"])
app.include_router(ai_router, tags=["IA"])