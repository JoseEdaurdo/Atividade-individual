# Estúdio Fotográfico

Este projeto é um sistema CRUD (Create, Read, Update, Delete) desenvolvido para gerenciar dados de forma simples e eficiente.

## Entidades e Relacionamentos

O sistema é composto por duas entidades principais:

### 1. Cliente
Representa uma pessoa que contrata ou agenda sessões.  
**Campos:**
- **id**  – Identificador único do cliente.
- **nome** – Nome completo do cliente.
- **email**  – E-mail único para contato.
- **telefone**  – Telefone de contato (apenas números).

### 2. Sessão
Representa um evento, serviço ou compromisso agendado para um cliente.  
**Campos:**
- **id** – Identificador único da sessão.
- **id_cliente** – Relaciona a sessão a um cliente específico.
- **data_sessao** – Data em que a sessão ocorrerá.
- **tipo_sessao** – Tipo ou categoria da sessão (ex.: aniversário, ensaio fotográfico, etc.).
- **local** – Local onde a sessão será realizada.
- **status** – Estado da sessão (ex.: Agendada, Concluída, Cancelada).

### Relacionamento
- Um **Cliente** pode ter várias **Sessões** (1:N).
- A chave estrangeira `id_cliente` na tabela `sessao` garante que cada sessão esteja vinculada a um cliente.
- A opção `ON DELETE CASCADE` garante que, ao excluir um cliente, todas as suas sessões também sejam excluídas automaticamente no banco de dados.

## Funcionalidades

- Cadastro de novos clientes e sessões
- Listagem dos clientes e sessões agendadas
- Atualização de informações
- Exclusão de registros

## Como Executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/JoseEdaurdo/Atividade-individual.git
    ```
2. Crie o ambiente virtual:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
3. Instale as dependências:
    ```bash
    pip install --upgrade pip
    pip install Flask
    ```
4. Execute o projeto:
    ```bash
    python run.py
    ```


