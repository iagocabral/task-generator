from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.ai_schema import GenerateTaskRequest
from app.schemas.task_schema import TaskResponse
from app.services.ai_service import generate_task_suggestions
from app.repositories.task_repository import create_task
from app.core.dependencies import get_current_user
from app.schemas.task_schema import TaskCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tasks/generate", response_model=list[TaskResponse])
def generate_tasks(request: GenerateTaskRequest, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    """
    Gera tarefas automaticamente com IA com base nas preferências do usuário.
    """
    if not request.preferences:
        raise HTTPException(status_code=400, detail="As preferências não podem estar vazias.")

    suggested_tasks = generate_task_suggestions(request.preferences)

    created_tasks = []
    for task_desc in suggested_tasks:
        task_data = TaskCreate(description=task_desc)  # Criar um objeto TaskCreate
        task = create_task(db, task_data, user_id)  # Passar um objeto TaskCreate corretamente
        created_tasks.append(task)

    return created_tasks