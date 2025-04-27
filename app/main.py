from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio
from datetime import datetime
from app.database import save_user, update_user_status, create_table
import uuid

app = FastAPI()

clients = []

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    client_id = str(uuid.uuid4())
    clients.append({"id": client_id, "socket": websocket})
    await save_user(client_id)

    try:
        while True:
            data = await websocket.receive_text()
            try:
                n = int(data.strip())
                result = fibonacci(n)
                await websocket.send_text(f"Fibonacci({n}) = {result}")
            except ValueError:
                await websocket.send_text("Erro: envie apenas um número inteiro.")
    except WebSocketDisconnect:
        clients[:] = [c for c in clients if c["id"] != client_id]
        await update_user_status(client_id, False)

@app.on_event("startup")
async def start_background_tasks():
    await create_table()
    asyncio.create_task(broadcast_datetime())

async def broadcast_datetime():
    while True:
        date = datetime.now().strftime("%d-%m-%Y")
        hour = datetime.now().strftime("%H:%M:%S")
        disconnected = []
        for client in clients:
            try:
                await client["socket"].send_text(f"Data: {date} Hora: {hour} UTC")
            except:
                disconnected.append(client)
        for client in disconnected:
            clients.remove(client)
        await asyncio.sleep(1)
