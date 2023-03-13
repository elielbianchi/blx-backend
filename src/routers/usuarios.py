from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Usuario
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.usuario import RepositorioUsuario

router = APIRouter()


@router.get("/usuarios", response_model=List[Usuario])
def listar_usuarios(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=Usuario)
def signup(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado
