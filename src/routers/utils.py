from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provider
from src.infra.sqlalchemy.repositories.usuario import RepositorioUsuario
from jose import JWTError

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


def obter_usuario_logado(token: str = Depends(oauth2_schema), session: Session = Depends(get_db)):
    TOKEN_EXCEPTION = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido')

    try:
        telefone = token_provider.verificar_acess_token(token)
    except JWTError:
        raise TOKEN_EXCEPTION

    if not telefone:
        raise TOKEN_EXCEPTION

    usuario = RepositorioUsuario(session).obter_por_telefone(telefone)

    if not usuario:
        raise TOKEN_EXCEPTION

    return usuario
