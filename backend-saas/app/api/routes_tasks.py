from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.task_schema import TaskCreate, TaskResponse
from app.repositories.task_repository import create_task, get_tasks_by_user, complete_task
from app.core.database import SessionLocal
from app.core.dependencies import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tasks", response_model=TaskResponse)
def add_task(task: TaskCreate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    return create_task(db, task, user_id)

@router.get("/tasks", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    return get_tasks_by_user(db, user_id)

@router.patch("/tasks/{task_id}", response_model=TaskResponse)
def mark_task_complete(task_id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    task = complete_task(db, task_id)
    if not task or task.user_id != user_id:
        raise HTTPException(status_code=403, detail="Acesso não permitido")
    return task