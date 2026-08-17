# FastAPI CRUD API - Curso Dunossauro

Repositório dedicado ao desenvolvimento de um projeto prático de CRUD utilizando FastAPI, desenvolvido durante os estudos do curso [FastAPI do Zero](https://fastapidozero.dunossauro.com/estavel/) do Dunossauro.

Este projeto marca a estruturação do meu primeiro ambiente de desenvolvimento backend, utilizando ferramentas modernas para gerenciamento de dependências, ambiente virtual e conteinerização.

## 🛠️ Tecnologias e Ferramentas

- **Python** (Linguagem da aplicação)
- **FastAPI** (Framework)
- **Poetry** (Gerenciamento do projeto e do ambiente virtual)
- **Pipx** (Instalação e execução de aplicações CLI Python em ambientes isolados)
- **Docker** (Conteinerização)
- **Git / gh** (Controle de versão)
- **Ruff** (Análise e formatação de código Python)
- **Pytest** (Testes automatizados)
- **Taskipy** (Atalhos para os comandos do projeto)

## Sobre o Projeto

O objetivo principal é aplicar os conceitos de desenvolvimento de APIs RESTful com FastAPI, estruturando um ambiente de desenvolvimento organizado e alinhado às boas práticas.

---
## Ao clonar o repositorio 

- Ative o ambiente
```
poetry shell 
```
- Instale as dependencias 
```
poetry install 
```

---

## Comando para usar o Ruff

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

Organiza automaticamente o código, como:

- indentação;
- espaçamento;
- quebras de linha;
- alinhamento;
- uso consistente de aspas (conforme a configuração do projeto).

```bash
poetry run ruff format
```

---

## Comando para usar o Pytest

Executa os testes automatizados e gera o relatório de cobertura no terminal.

```bash
pytest --cov=dunossauro_fastapi -v
```

Gera um relatório de cobertura em HTML na pasta `htmlcov`.

```bash
poetry run coverage html
```

> **Obs.:** Após gerar o relatório, abra o arquivo `http://localhost:5500/htmlcov/index.html` no navegador para visualizar os detalhes da cobertura dos testes.

---

## Atalhos Taskipy: comandos para rodar, testar e formatar a aplicacao

Verifique se o ambiente virtual está ativado. Caso não esteja, execute:

```bash
poetry shell
```

Após acessar o ambiente, utilize os comandos abaixo.

Verifica problemas no código.

```bash
task lint
```

Formata o código conforme a configuração do projeto.

```bash
task format
```

Executa a aplicação.

```bash
task run
```