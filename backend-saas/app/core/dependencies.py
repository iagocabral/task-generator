from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from app.core.security import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: str = Security(oauth2_scheme)):
    payload = verify_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")
    return payload["sub"]  # Retorna o ID do usuário autenticado