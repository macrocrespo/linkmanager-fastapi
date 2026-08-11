from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy import text
from app.infrastructure.db.session import engine
from app.presentation.api.v1.routers import tags
from app.domain.exceptions import TagAlreadyExists

app = FastAPI(title="Link Manager")

@app.get("/")
async def root():
    return {"message": "Hello World, Link Manager here!"}

@app.get('/health')
async def health():
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
    return {"status": "ok"}

app.include_router(tags.router)

@app.exception_handler(TagAlreadyExists)
async def tag_already_exists_handler(request: Request, exc: TagAlreadyExists):
    return JSONResponse(status_code=409, content={"detail": str(exc)})