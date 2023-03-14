from sqlalchemy import update, delete, select
from sqlalchemy.orm import Session
from typing import List
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioPedido():

    def __init__(self, session: Session) -> None:
        self.session = session

    def gravar_pedido(self, pedido: schemas.Pedido) -> models.Pedido:
        db_pedido = models.Pedido(quantidade=pedido.quantidade,
                                  local_entrega=pedido.local_entrega,
                                  tipo_entrega=pedido.tipo_entrega,
                                  observacao=pedido.observacao,
                                  usuario_id=pedido.usuario_id,
                                  produto_id=pedido.produto_id)
        self.session.add(db_pedido)
        self.session.commit()
        self.session.refresh(db_pedido)
        return db_pedido

    def buscar_por_id(self, id: int) -> models.Pedido:
        query = select(models.Pedido).where(models.Pedido.id == id)
        pedido = self.session.execute(query).scalars().one()
        return pedido

    def listar_meus_pedidos_por_usuario_id(self, usuario_id: int) -> List[models.Pedido]:
        query = select(models.Pedido).where(
            models.Pedido.usuario_id == usuario_id)
        pedidos = list(self.session.execute(query).scalars().all())
        return pedidos

    def listar_minhas_vendas_por_usuario_id(self, usuario_id: int) -> List[models.Pedido]:
        query = select(models.Pedido).join_from(models.Pedido, models.Produto).where(
            models.Produto.usuario_id == usuario_id)
        pedidos = list(self.session.execute(query).scalars().all())
        return pedidos
