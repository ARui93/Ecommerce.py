# Projeto em Desenvolvimento: API de E-commerce

Este projeto visa desenvolver uma API de e-commerce utilizando Python e Flask para aprimorar habilidades em desenvolvimento de APIs. Utilizamos o Postman para testar e validar as funcionalidades implementadas.

## Descrição

O projeto consiste em uma API que oferece diversas funcionalidades essenciais para um sistema de e-commerce, incluindo autenticação de usuários, gerenciamento de produtos e manipulação de carrinho de compras. O objetivo é demonstrar como desenvolver e testar APIs de forma eficiente utilizando Flask.

## Funcionalidades Implementadas

### Autenticação de Usuário

A API possui endpoints para login e logout de usuários. Utilizamos autenticação baseada em tokens para garantir a segurança das operações.

### Gerenciamento de Produtos

- **Adicionar Produto**: Endpoint para adicionar novos produtos ao banco de dados.
- **Atualizar Produto**: Endpoint para atualizar informações de um produto existente.
- **Excluir Produto**: Endpoint para remover um produto do banco de dados.
- **Buscar Produtos**: Endpoint para listar todos os produtos disponíveis.

### Carrinho de Compras

- **Adicionar ao Carrinho**: Endpoint para adicionar produtos ao carrinho de compras de um usuário autenticado.
- **Remover do Carrinho**: Endpoint para remover produtos do carrinho de compras.
- **Visualizar Carrinho**: Endpoint para visualizar o conteúdo atual do carrinho de compras de um usuário.
- **Checkout**: Endpoint para finalizar a compra, limpando o carrinho de compras após o checkout.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flask**: Framework web utilizado para desenvolver a API.
- **SQLAlchemy**: Biblioteca para interação com banco de dados SQL.
- **Postman**: Ferramenta utilizada para testar e validar as APIs desenvolvidas.

## Como Executar

Para executar o projeto localmente:

1. Clone o repositório para sua máquina.
2. Instale as dependências utilizando o comando `pip install -r requirements.txt`.
3. Execute o aplicativo Flask com o comando `python app.py`.
4. Utilize o Postman ou outro cliente HTTP para interagir com os endpoints da API.

