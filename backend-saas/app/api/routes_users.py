from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserResponse
from app.repositories.user_repository import create_user, get_all_users, get_user_by_email
from app.core.database import SessionLocal

router = APIRouter()

# Dependência para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para criar um novo usuário
@router.post("/users", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    return create_user(db, user)

# Rota para listar todos os usuários (sem a senha)
@router.get("/users", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    users = get_all_users(db)
    return users
