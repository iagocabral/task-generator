from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task_schema import TaskCreate

def get_tasks_by_user(db: Session, user_id: int):
    return db.query(Task).filter(Task.user_id == user_id).all()

def create_task(db: Session, task: TaskCreate, user_id: int):
    db_task = Task(description=task.description, user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def complete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.completed = True
        db.commit()
        db.refresh(task)
    return task