# Ao clonar o repositório

* Ative o ambiente virtual:

```bash
poetry shell
```

* Instale as dependências:

```bash
poetry install
```

# Crie o `.env`

Na raiz do projeto, crie um arquivo `.env` com:

```env
DATABASE_URL="sqlite:///./database.db"
```

# Execute as migrations

Execute o comando do Alembic para criar/atualizar as tabelas do banco de dados:

```bash
alembic upgrade head
```
