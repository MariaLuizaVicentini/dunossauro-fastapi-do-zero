# Aplicacoes web

Sempre quando estamos falando de sistemas web, estamos falando de sistemas que funcionam em REDE.

A rede é o que permite a conexao e comunicaco de um ou mais disposivitos.


Rede - LAN
- Rede local curta distancia que temos dentro de casa

Rede - WAN
- Rede de longa distancia que conecta cidades 

Rede - MUNDIAL
- Rede de longa distancia como a propria internet

---

## Comunicao do tipo cliente-servidor

Existem diversos tipos de comunicacao alem dessa, mas a mais importante e essa.

Nesse modelo, temos duas principais entidades:

Cliente
- Faz requisicoes / solicitacoes pro servidor
- Obtem respostas apos solicitacao

Servidor
- Serve a aplicacao pro cliente
- O responsavel por processar as requisicoes e devolver uma resposta pro client

Aplicaco python
- cod font e dependencias da app


---

# Diferença entre fastAPI e Uvicorn

o fastapi é um framework web que nao tem um servidor de aplicaco, mas possui o uvicorn que é em essencia o servidor da app

O fastapi serve cod, mas nao se auto  quem serve a aplicao na rede é o uvicorn

uvicorn e responsavel por receber as chamadas de rede e repassar isso pro codigo puro

[ Client ]  ←→ requisicao ←→  [ uvicorn ]  ←→ repassa ←→ [ app python ]

---

# Loopback

Um loop de solicitacao e retorno

Usamos a rede local pra codar e testar a app, portanto, o nosso pc é o CLIENTE e também o SERVIDOR ao mesmo tempo.

---

# IP da minha maquina

'172.31.93.235'