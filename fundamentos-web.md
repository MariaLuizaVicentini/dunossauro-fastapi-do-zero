# Aplicações Web

Sempre que falamos de sistemas web, estamos falando de sistemas que funcionam em uma **rede**.

A rede é o que permite a conexão e a comunicação entre um ou mais dispositivos.

## Tipos de rede

### LAN (Local Area Network)
- Rede local de curta distância.
- Exemplo: rede de uma casa ou escritório.

### WAN (Wide Area Network)
- Rede de longa distância.
- Conecta cidades, estados e países.

### Rede mundial
- A própria Internet.
- Rede que conecta dispositivos no mundo todo.

---

# Comunicação cliente-servidor

Existem diversos modelos de comunicação, mas o mais comum em aplicações web é o **cliente-servidor**.

Nesse modelo existem duas entidades principais:

## Cliente
- Faz requisições ao servidor.
- Recebe uma resposta após a solicitação.

## Servidor
- Disponibiliza a aplicação para o cliente.
- Processa as requisições.
- Retorna uma resposta ao cliente.

## Aplicação Python
- Contém o código-fonte e as dependências da aplicação.

---

# Diferença entre FastAPI e Uvicorn

O **FastAPI** é um framework web. Ele **não possui um servidor de aplicação próprio**.

O **Uvicorn** é o servidor responsável por disponibilizar a aplicação na rede.

Enquanto o FastAPI define o comportamento da aplicação, o Uvicorn recebe as requisições da rede e as repassa para o código Python.

```text
[ Cliente ] ←→ requisição ←→ [ Uvicorn ] ←→ [ Aplicação Python (FastAPI) ]
```

---

# Loopback

É o cenário em que utilizamos a própria máquina para fazer requisições à aplicação.

Durante o desenvolvimento, o computador atua como **cliente** e **servidor** ao mesmo tempo.

---

# Modelo padrão da Web

## URL
- É um endereço de rede utilizado para acessar um dispositivo ou serviço.

### Protocolo
- Indica o protocolo utilizado para a comunicação.

```text
http://
```


### Endereço
- Indica o endereço (ou domínio) do dispositivo onde a aplicação está sendo executada.

```text
127.0.0.1
```


### Porta
- Indica a porta utilizada para estabelecer a comunicação com a aplicação.

```text
:8000
```


### Caminho
- Onde está o que queremos acessar
```
/caminho
```

### Recurso
- A identificacao do que queremos
```
/recurso
```

### Query
- Um filtro do recurso
```
?query
```

### Fragmento
- Especifica um pedaço do recurso
```
#fragmento
```

---

## HTTP

- É um protocolo de transferencia de Hipertexto
- É o protocolo fundamental na web pra transferencia de dados e comunicacao entre clientes e servidores
- Ele baseia-se no modelo de requisicao-resposta: onde o cliente faz um requisicao ao servidor, que responde a essa requisicao. 
- Essas requisicoes e respostas sao formatadas conforme as regras de protocolo HTTP

---

