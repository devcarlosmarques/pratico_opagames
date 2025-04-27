import asyncpg

async def connect():
    return await asyncpg.connect(
        user='user',
        password='password',
        database='websocket_db',
        host='db'
    )

async def create_table():
    conn = await connect()
    await conn.execute("""
        CREATE TABLE IF NOT EXISTS user_registration (
            id SERIAL PRIMARY KEY,
            client_id TEXT NOT NULL,
            last_activity TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_active BOOLEAN NOT NULL
        );
    """)
    await conn.close()

async def save_user(client_id):
    conn = await connect()
    await conn.execute(
        "INSERT INTO user_registration (client_id, is_active) VALUES ($1, $2)",
        client_id, True
    )
    await conn.close()

async def update_user_status(client_id, is_active):
    conn = await connect()
    await conn.execute(
        "UPDATE user_registration SET is_active = $1, last_activity = CURRENT_TIMESTAMP WHERE client_id = $2",
        is_active, client_id
    )
    await conn.close()
