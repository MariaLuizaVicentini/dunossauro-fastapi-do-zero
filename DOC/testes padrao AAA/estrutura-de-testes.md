# O que é a estrutura AAA de Testes

Todo teste vai ficar dentro da pasta "tests" que faz parte da raiz da app:
- Além disso, todo arquivo de teste e toda funcao de teste deve começar com "test_nometeste"

---

A ideia é que todo e qualquer teste por padrao tenha esssas tres etapas, sempre nessa ordem:

1) A = Arranjo (Preparar)
2) A = Acao (Agir)
3) A = Verificar
---



## Primeira etapa: Arranjo (Preparar)

Nessa etapa montamos tudo o que o teste precisa pra acontecer

Ex:
- Criar objetos
- preparar dados de entrada
- configurar mocks se necessarii
- inicializar o cliente de testes (TestClient)

```python
    from fastapi.testclient import TestClient

    client = TesteClient(app)
```
```python
usuario = {'nome': 'Maluzera', 'idade': 23}
```

---
## Segunda etapa: Acao (Agir)

Aqui executamos exatamente a acao que desejamos testar.

Ex:
- Chamar uma funcao de um arquivo
- Fazer uma requesicao para uma API

```python
response = client.get('/')
```

```python
    resultado = sum(2, 3)
```
---

## Terceira etapa: Verificar (Garantir)

Aqui confirmamos se o resultado obtido atende ao resultado esperado. 

Ex:
- Ao chamar o "/" o uma mensagem "Hello world!" o deve ser exibida

ACAO
```python
response = client.get('/')
```
VERIFICACAO/RESULTADO
```python
    {'message': 'Hello world!'}
```

## Juntando as peças soltas

Escrevendo o teste em linguagem natural:
```bash
Dado: Que o exista um client http inicializado
Quando: O cliente HTTP chamar "/"
Entao: Uma mensagem "Hello world!" deve ser exibida com sucesso
```

Escrevendo o teste com python:
```python
from http import HTTPStatus

from fastapi.testclient import TestClient

from dunossauro_fastapi.app import app


# dado
client = TesteClient(app)
# entao
resonse = client.get('/')
# verificacao
assert response.json() == {'message': 'Hello world!'}
assert response.status_code == HTTPStatus.OK
```