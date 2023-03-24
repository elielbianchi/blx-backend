from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])


def gerar_hash(texto: str) -> str:
    return pwd_context.hash(texto)


def verificar_hash(texto, hash) -> bool:
    return pwd_context.verify(texto, hash)
