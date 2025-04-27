# Teste Prático - OpaGames

Este projeto é um app websocket desenvolvido em Python com FastAPI, que oferece:

- Conexão via WebSocket para múltiplos clientes
- Envio da data/hora atual a cada segundo para todos os clientes conectados
- Cálculo de fibonacci de forma manual
- Gestão de usuários conectados via banco de dados PostgreSQL
- Containerização completa com Docker

---

## Tecnologias Utilizadas

- **Python 3.11**
- **FastAPI**
- **WebSocket**
- **asyncio**
- **asyncpg**
- **PostgreSQL**
- **Docker**

---

## Como Rodar o Projeto

### 1. Softwares Necessarios

- *Docker Desktop*

### 2. Comandos para executar a aplicação [servidor]

git clone "link_do_repositorio"
cd teste_pratico_opagames
docker compose up -d --build

### 2. Como testar a aplicação [cliente]

Você pode usar qualquer cliente WebSocket para testar a conexão.
Exemplo: Postman
URL: ws://localhost:8000/ws

Ao conectar:
Você receberá mensagens como (DATA: DD-MM-AAAA HORA: HH-MM-SS UTC) a cada segundo.
Envie um número (ex: 10) e receberá Fibonacci(10) = 55
obs: forneça apenas numeros inteiros(1,2,3,4).


