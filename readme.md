# Teste Prático - OpaGames

Este projeto é uma aplicação WebSocket desenvolvida em **Python** com **FastAPI**, que oferece:

- Conexão via WebSocket para múltiplos clientes
- Envio da data/hora atual a cada segundo para todos os clientes conectados
- Cálculo de números de Fibonacci sob demanda
- Gestão de usuários conectados utilizando **PostgreSQL**
- Containerização completa com **Docker**

## Tecnologias Utilizadas

- Python 3.11
- FastAPI
- WebSocket
- asyncio
- asyncpg
- PostgreSQL
- Docker

## Como Rodar o Projeto

### 1. Pré-requisitos

- Docker Desktop instalado na sua máquina

### 2. Passos para executar o servidor

```bash
git clone "link_do_repositorio"
cd teste_pratico_opagames
docker compose up -d --build
```

## Como Testar a Aplicação

Você pode usar qualquer cliente WebSocket para testar a conexão. Exemplo: **Postman**.

- **URL:** `ws://localhost:8000/ws`

### Comportamento esperado:

- **Ao conectar:** Você começará a receber mensagens com a data e hora atual no formato:

  ```
  DATA: DD-MM-AAAA HORA: HH-MM-SS UTC
  ```
  enviadas a cada segundo.

- **Para calcular Fibonacci:** Envie um número inteiro (ex: `10`) e você receberá a resposta:

  ```
  Fibonacci(10) = 55
  ```

>  Obs: Envie apenas números inteiros positivos (ex: 1, 2, 3, 4...).
