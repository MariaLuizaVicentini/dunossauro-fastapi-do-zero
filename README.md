# FastAPI CRUD API - Curso Dunossauro

Repositório dedicado ao desenvolvimento de um projeto prático de CRUD utilizando FastAPI, construído durante os estudos do curso [FastAPI do Zero](https://fastapidozero.dunossauro.com/estavel/) do Dunossauro. 

Este projeto marca a estruturação do meu primeiro ambiente de desenvolvimento profissional backend, integrando ferramentas modernas de isolamento, gerenciamento de pacotes e conteinerização.

## 🛠️ Tecnologias e Ferramentas

- **Python** (Principal tecnologia da app)
- **FastAPI** (Framework)
- **Poetry** (Gerencia o projeto e o ambiente virtual)
- **Pipx** (Instalação e execução de aplicações CLI Python em ambientes isolados)
- **Docker** (Conteinerização do ambiente)
- **Git / gh** (Controle de versão)
- **Ruff** (analisa e formata o código Python)
- **Pytest** (Pra escrever os testes)
- **Taskpy** (Pra nao ter que lembrar todos os comandos da app)


## Sobre o Projeto

O objetivo principal é aplicar os conceitos fundamentais e avançados de desenvolvimento de APIs RESTful com FastAPI, estruturando um ambiente de desenvolvimento robusto, reprodutível e alinhado com as melhores práticas de mercado.


----

## Comando pra rodar a aplicacao

Comando pra rodar a aplicao até o momento com o poetry

```bash
poetry run fastapi dev dunossauro_fastapi/app.py
```

Esse tambem serve:

```bash
fastapi dev dunossauro_fastapi/app.py
```
---

## Comando pra rodar o Ruff

### Listar os subcomandos disponíveis

```bash
poetry run ruff
```

### Analisar o código (lint)

Procura problemas no código, como:
- imports não utilizados;
- erros de estilo;
- possíveis bugs;
- código que não segue as regras configuradas.

```bash
poetry run ruff check
```

### Formatar o código

Organiza automaticamente a aparência do código, como:
- indentação;
- espaçamento;
- quebras de linha;
- alinhamento;
- uso consistente de aspas (conforme a configuração do projeto).

```bash
poetry run ruff format
```
---

## Comando para usar o pytest

- Executa os testes automatizados do projeto e gera o relatório de cobertura no terminal.
```bash
pytest --cov=dunossauro_fastapi -v
```

- Gera um relatório de cobertura em HTML na pasta `htmlcov`.
```bash
poetry run coverage html
```

> **Obs.:** Após gerar o relatório, abra o arquivo `http://localhost:5500/htmlcov/index.html` no navegador para visualizar os detalhes da cobertura dos testes.

---

## Comando para usar o taskipy