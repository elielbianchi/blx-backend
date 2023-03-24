from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from src.routers import produtos, pedidos, auth
from src.jobs.write_notification import write_notification

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

# SEGURANÇA: Autenticação e Autorização
app.include_router(auth.router, prefix="/auth")

# PEDIDOS
app.include_router(pedidos.router)


# EXEMPLO TAREFA BACKGROUND
@app.post('/send-email/{email}')
def send_email(email: str, mensagem: str, background: BackgroundTasks):
    background.add_task(write_notification,
                        email, 'Mensagem de exemplo')

    return {'OK': 'Mensagem enviada'}

# MIDDLEWARES


@app.middleware('http')
async def processar_tempo_requisicao(request: Request, next):
    print('Interceptou a chegada...')

    response = await next(request)

    print('Interceptou volta...')

    return response
