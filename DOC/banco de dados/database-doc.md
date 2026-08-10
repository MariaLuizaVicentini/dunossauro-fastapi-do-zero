
# SQLAlchemy

- é uma lib em python que permite trabalhar com banco de dados relacionais.
- O ORM é um componente dessa lib que permite representar elementos do banco de dados como objetos/classes em python.

```
PYTHON       ---- >    BANCO DE DADOS
- Classes              - Tabelas
- Objetos              - Registros
- Atributos            - Colunas
```

- Ao inves de mexer com SQL o tempo todo, a app pode trabalhar atraves das estruturas pyhton do ORM. 
- O SQLAlchemy também pode trabalhar diretamente com SQL, mas o ORM é justamente a camada que faz esse mapeamento entre objetos Python e dados relacionais.

### Session
- Representa uma sessao de integracao com o banco de dados
- Responsavel por gerenciar o trabalho que a app esta fazendo com os objetos do ORM e coordenar operacoes como:
    - consultar dados
    - add objetos
    - alterar objetos
    - controlar transacoes
    - enviar alteracoes para o banco atraves do `commit`

```
APLICACAO
  |
Session
  |
SQLALchemy
  |
Banco de dados
```
- A Session tambem mantem o chamado estado dos objetos que estao sendo trabalhados naquela sessao

### Engine

- É o componente responsavel por fazer a ponte entre o SQLAlchemy e o banco de dados

Ele sabe, entre outras coisas:
- qual banco sera utilizado
- como se conectar a ele
- qual drive utilizar

```
Aplicação
  |
SQLAlchemy
  |
Engine
  |
Conexão / Pool
  |
Banco de dados
```
O Engine é criado a partir da URL de conexão do banco.

Ex:
```
sqlite:///database.db
```

O Engine não representa uma única conexão aberta permanentemente. Ele gerencia um pool de conexões e fornece conexões quando necessário.

### Models
- Os models sao as representacoes das entidades do banco de dados dentro da app
- No SQLAlchemy ORM, normalmente sao classes Python que representam tabelas

```
Model Python
  |
Tabela do banco

User
  |
users

User.name
  |
users.name
```

Um model normalmente define:
- qual tabela representa
- quais colunas existem
- tipos das colunas
- chaves primarias
- relacionamentos
- outras caracteristicas da estrutura dos dados

```python
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())

```

Por isso, o Model funciona como uma representação da estrutura de uma tabela dentro do código Python.


### Hooks, Eventos - SQLAlchemy
- Eventos sao mecanismos que permitem executar alguma logica quando determinados acontecimentos ocorrem dentro do SQLAlchemy
- Eles funcionam como pontos de observação/interceptação do comportamento do SQLAlchemy.

Eventos podem estar relacionados a:
- Cricao de uma conexao
- execucao do SQL
- insercao, alteracao, remocao de objetos
- acoes relacionadas a Session
- ciclo de vida dos objetos ORM

```
Acontecimento no SQLAlchemy
          ↓
       EVENTO
          ↓
   lógica adicional
```


# Harlequin - Visualizacao do database.db via terminal

O Harlequin é uma ferramenta de terminal para trabalhar e visualizar bancos de dados.

No meu caso, você está utilizando ele para abrir o banco SQLite:

````
database.db
````

Comando para ter a visualizacao via terminal:
- Dentro do projeto:

````bash
harlequin database.db
````
