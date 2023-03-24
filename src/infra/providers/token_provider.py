from datetime import datetime, timedelta
from jose import jwt

# CONFIG
SECRET_KEY = '7ab687dce2372ab6bc9bbabf09f126ed'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 1440


def criar_acess_token(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    dados.update({'exp': expiracao})

    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt


def verificar_acess_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get('sub')
