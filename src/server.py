from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, Usuario
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositories.produto import RepositorioProduto
from src.infra.sqlalchemy.repositories.usuario import RepositorioUsuario

# criar_bd()

app = FastAPI()

# PRODUTOS


@app.get("/produtos", response_model=List[Produto])
def listar_produtos(session: Session = Depends(get_db)):
    produtos = RepositorioProduto(session).listar()
    return produtos


@app.post("/produtos", status_code=status.HTTP_201_CREATED, response_model=Produto)
def criar_produto(produto: Produto, session: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(session).criar(produto)
    return produto_criado


# USUARIOS

@app.get("/usuarios", response_model=List[Usuario])
def listar_usuarios(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios


@app.post("/usuarios", status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado
