# Documentacao das configuracoes de projeto

Esse documento tem como objetivo explicar as configs atuais da aplicacao gerenciadas no arquivo:
-  **" ⚙️pyproject.toml "**


----

O `pyproject.toml` é o arquivo central de configuração de um projeto Python. Nele ficam as informações do projeto e as configurações das ferramentas utilizadas no desenvolvimento.

## Principais tabelas da aplicacao

### `[project]`
Define a identidade da aplicação e seus metadados.
Contém informações como:
- nome
- dependências de produção pra app funcionar

```bash
    [project]
    name = "dunossauro-fastapi"
    version = "0.1.0"
    description = "Meu primeiro projeto com ambiente de desenvolvimento config"
    authors = [
        {name = "Maria Luiza",email = "vicentinimalu1@gmail.com"}
    ]
    readme = "README.md"
    requires-python = ">=3.12,<4.0"
    dependencies = [
        "fastapi[standard] (>=0.141.1,<0.142.0)"
    ]
```


> É a seção que descreve **o que é o projeto e o que ele precisa pra funcionar**.

---

### `[build-system]`
Define como o projeto será construído e empacotado.
Informa:
- qual ferramenta fará o build (requires)
- o backend de build que executará esse processo (build-backend)


```bash
    [build-system]
    requires = ["poetry-core>=2.0.0,<3.0.0"]
    build-backend = "poetry.core.masonry.api"
```

> É a seção que define **qual ferramenta e quais dependências são usadas para construir e empacotar o projeto**.
---

### `[dependency-groups]`
Organiza as dependências utilizadas durante o desenvolvimento, separando-as em grupos conforme sua finalidade.
Normalmente são incluídas ferramentas como:
- testes (`pytest`)
- lint (`ruff`)
- cobertura de testes (`coverage`)
- documentação
- outras ferramentas de desenvolvimento

```bash
    [dependency-groups]
    dev = [
        "ruff (>=0.16.1,<0.17.0)",
        "pytest (>=9.1.1,<10.0.0)",
        "pytest-cov (>=7.1.0,<8.0.0)",
        "taskipy (>=1.14.1,<2.0.0)"
    ]
```

> É a seção usada para agrupar dependências que são necessárias apenas para o ambiente de desenvolvimento e testes, sem fazer parte das dependências de produção da aplicação

---

### `[tool]`
Centraliza as configurações das ferramentas utilizadas no projeto.
Exemplos:
- Ruff
- Pytest
- Coverage
- taskipy

```bash
    # Configurações do Ruff (lint e formatação de código)
    [tool.ruff]
    line-length = 79
    extend-exclude = ['migrations']

    # Regras da análise estática da estética do codigo fonte (lint)
    [tool.ruff.lint]
    preview = true
    select = ['I', 'F', 'E', 'W', 'PL', 'PT']

    # Configurações do formatador de código
    [tool.ruff.format]
    preview = true
    quote-style = 'single'


    # Configurações do Pytest (execução dos testes)
    [tool.pytest.ini_options]
    pythonpath = '.'
    addopts = '-p no:warnings'


    # Tarefas/atalhos personalizadas executadas pelo Taskipy
    [tool.taskipy.tasks]
    #Analisa o código e aponta erros e problemas de estilo.
    lint = 'ruff check' 
    # Formata o código (indentação, aspas, espaços, etc.).
    format = 'ruff format'
    # Corrige automaticamente problemas. É executada antes da task format.
    pre_format = 'ruff check --fix'
    # Inicia a aplicação FastAPI em modo de desenvolvimento.
    run = 'fastapi dev fast_zero/app.py'
    # Executa o lint antes de rodar os testes.
    pre_test = 'task lint'
    # Executa os testes, mostra detalhes e gera a cobertura do pacote fast_zero.
    test = 'pytest -s -x --cov=fast_zero -vv'
    # Gera um relatório HTML da cobertura de testes após a execução do pytest.
    post_test = 'coverage html'
```


No dia a dia:
1 - **task run**: inicia a aplicacao
2 - **task format**: formata automaticamente
3 - **task test**: executa os testes na pasta de testes
4 - **git add**: add modificacoes no projeto
5 - **git commit**: registra mensagem de commit 
5 - **git push**: envia as alteracoes comitadas pra branch 


> É a seção onde **cada ferramenta armazena suas configurações e comandos**, concentrando tudo em um único arquivo de configuração (`pyproject.toml`).
