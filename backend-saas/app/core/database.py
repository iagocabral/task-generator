import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
#DATABASE_URL = os.getenv("DATABASE_URL_TEST")  # Banco de testes

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Importar os modelos para criar as tabelas
from app.models.user import User
from app.models.task import Task

def create_tables():
    Base.metadata.create_all(bind=engine)

# 🔹 Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()