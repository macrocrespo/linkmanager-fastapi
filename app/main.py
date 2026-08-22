from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy import text
from app.infrastructure.db.session import engine
from app.domain.exceptions import TagAlreadyExists
from app.domain.exceptions import UserAlreadyExists
from app.domain.exceptions import InvalidCredentials

from app.presentation.api.v1.routers import tags, auth, links

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
app.include_router(auth.router)
app.include_router(links.router)

@app.exception_handler(TagAlreadyExists)
async def tag_already_exists_handler(request: Request, exc: TagAlreadyExists):
    return JSONResponse(status_code=409, content={"detail": str(exc)})

@app.exception_handler(UserAlreadyExists)
async def user_already_exists_handler(request: Request, exc: UserAlreadyExists):
    return JSONResponse(status_code=409, content={"detail": str(exc)})

@app.exception_handler(InvalidCredentials)
async def invalid_credentials_handler(request: Request, exc: InvalidCredentials):
    return JSONResponse(status_code=401, content={"detail": str(exc)})