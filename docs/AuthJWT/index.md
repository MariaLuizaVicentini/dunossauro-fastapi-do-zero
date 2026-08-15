# Armazenamento seguro de senhas

Senhas de usuários não devem ser armazenadas no banco de dados em texto puro. Para armazená-las de forma segura, utilizamos funções de hash específicas para senhas.

Neste projeto, vamos utilizar:
```
poetry add "pwdlib[argon2]"
```
- `pwdlib`: É uma biblioteca utilizada para trabalhar com hashes de senhas.
    - `PasswordHash`: É um objeto utilizado para gerar e verificar hashes de senhas
- `argon2`: É um algoritmo de hash de senhas utilizado pelo pwdlib


### Hash de senha
Hash não é criptografia.

Um hash é uma transformação unidirecional: a partir de uma senha, podemos gerar um hash, mas não conseguimos usar o hash para simplesmente "descriptografar" e recuperar a senha original.

Por isso, em vez de armazenar a senha do usuário diretamente no banco, armazenamos seu hash.

---

# Autenticação vs Autorização

Apesar de serem conceitos relacionados, autenticação e autorização são coisas diferentes.

`Autenticação`
- É o processo de verificar quem é o usuário.

`Autorização`
- É o processo de verificar o que o usuário tem permissão para fazer.

---

# O Token JWT

De forma simples, JWT (JSON Web Token) é um formato padronizado para transmitir informações entre partes de forma compacta.

Em uma aplicação com autenticação, o servidor pode emitir um JWT depois que o usuário apresenta credenciais válidas.

Por exemplo:

1. O cliente envia username e password.
2. O servidor verifica essas credenciais.
3. Se estiverem corretas, o servidor gera um JWT.
4. O cliente passa a enviar esse token nas requisições que precisam de autenticação.
5. O servidor verifica se o token é válido e, a partir dele, identifica o usuário.

É como se o servidor disse:<br>

- *Eu, servidor, gerei este token e assinei seu conteúdo. Se alguém alterar o conteúdo do token, a assinatura não será mais válida*

Importante: 
- JWT não significa que o servidor está dizendo simplesmente que "o usuário existe no banco". 
- O token contém informações (claims) que o servidor escolheu colocar nele, e a assinatura permite verificar que essas informações não foram alteradas e que o token foi produzido por quem possui a chave utilizada para assiná-lo.

## Estrutura de um JWT:

Divido em 3 partes:
```
HEADER.PAYLOAD.SIGNATURE
```
Ex:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJzdWIiOiJtYWx1emVpcmEifQ.
yu7NrPIlfPPddCNjAaj5tck1Qkuos3XKpSBNgy25cA4
```

`Header`
- O Header contém informações sobre o token, principalmente:
    - o algoritmo utilizado para a assinatura (alg);
    - o tipo do token (typ).
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

`Payload`
- O Payload contém os dados que queremos transportar dentro do token. 
- Esses dados sao chamados de claims
```json
{
  "sub": "maluzeira",
  "exp": 1780000000
}
```
- O payload e header não é criptografado por padrão


`Assinatura`
- Ela é utilizada para verificar se o token foi alterado e, dependendo do algoritmo utilizado, para verificar que ele foi produzido por quem possui a chave necessária para assiná-lo.
- No caso do HS256, temos uma chave secreta compartilhada.

## Geracao de tokens com Pyjwt

- Existem diversas libs que geral tokens, vamos usar essa:
```
poetry add pyjwt
```

Existem 2 funcoes principais:

Depois de instalar a biblioteca, podemos abrir o Python no ambiente do projeto:
```
poetry shell
```
```
python
```

No modo interativo:
```
>>> import jwt
```
```python
>>> jwt.encode(
        {'sub': 'maluzeira'},
        'senha123',
        algorithm="HS256"
    )
```
O resultado esperado seria:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtYWx1emVpcmEifQ.yu7NrPIlfPPddCNjAaj5tck1Qkuos3XKpSBNgy25cA4
```


Se acessarmos o site:
```
https://www.jwt.io/
```

E colarmos o token JWT gerado, vamos conseguir deocdificar o header e tambem o payload, mas nao a senha.