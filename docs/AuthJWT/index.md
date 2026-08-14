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