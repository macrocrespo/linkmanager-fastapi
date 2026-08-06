from fastapi import FastAPI
from sqlalchemy import text
from app.infrastructure.db.session import engine

app = FastAPI(title="Link Manager")

@app.get("/")
async def root():
    return {"message": "Hello World, Link Manager here!"}

@app.get('/health')
async def health():
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
    return {"status": "ok"}