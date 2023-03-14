from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import produtos, usuarios, pedidos

app = FastAPI()

# CORS
origins = ['http://localhost:3000']

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

# PRODUTOS
app.include_router(produtos.router)

# USUARIOS
app.include_router(usuarios.router)

# PEDIDOS
app.include_router(pedidos.router)
