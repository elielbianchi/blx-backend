# blx-backend

### Descrição

Esta API foi desenvolvida com objetivos didáticos de explorar conhecimentos em novas tecnologias;
A proposta desta API é cadastrar, ler, atualizar e deletar produtos (CRUD) que possam ser anunciados em uma plataforma de vendas. Qualquer usuário pode anunciar e realizar pedidos de produtos;

Créditos ao prof. Rogério Silva (https://www.rogeriosilva.dev/), que desenvolveu esta API durante as suas aulas disponibilizadas.

### Estrutura

- API utilizando Python com o framework FastAPI, com a library Pydantic

- API REST e utilizando de estrutura MVC;

- Banco de dados: SQL com utilização do SQL Alchemy

### Banco de dados

A estrutura do banco de dados é separada em 3 classes principais que possuem atributos conforme abaixo:

- Usuário: id, nome, senha (hash), telefone, produtos(anunciados), pedidos(realizados);
- Produto: id, nome, detalhes, preco, disponivel(sim ou não), tamanhos, usuario_id(anunciante);
- Pedido: id, quantidade, local_entrega, tipo_entrega, observacao, usuario_id(que comprou), produto_id(comprado);


### Rotas

As rotas desenvolvidas são as que seguem abaixo:

USUÁRIO
- signup (POST "/signup");
- login (POST "/token");
- me (GET "/me")

PRODUTOS
- listar_produtos (GET "/produtos")
- exibir_produto (GET "/produtos/{id}")
- criar_produto (POST "/produtos")
- atualizar_produto(PUT "/produtos/{id}");
- remover_produto(DELETE "/produtos/{id}");

PEDIDOS
- listar_pedidos (GET "/pedidos");
- listar_vendas (GET "/pedidos/{usuario_id}/vendas")
- exibir_pedido (GET "/pedidos/{id}")
- fazer_pedido (POST "/pedidos")


### Tecnologias

- Python 3 (https://www.python.org/downloads/)
- FastAPI (https://fastapi.tiangolo.com/tutorial/)
- SQL Alchemy (https://www.sqlalchemy.org/download.html)
- Pydantic (https://docs.pydantic.dev/latest/install/)
- Hash com JWT Token (https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

### Rodar o projeto


Para rodar o projeto, é preciso instalar todas as dependências conforme listadas acima na seção de Tecnologias. Após isso, o FastAPI disponibiliza para executar o servidor local a lib "Uvicorn", que pode rodar o projeto através do terminal com a seguinte linha de comando: ```uvicorn src.server:app```

O FastAPI já disponibiliza o Swagger UI, o qual abre pelo navegador web localmente uma interface documentada das rotas e tipos de dados para envio a API. 
