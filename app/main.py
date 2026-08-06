from fastapi import FastAPI

app = FastAPI(title="Link Manager")

@app.get("/")
async def root():
    return {"message": "Hello World, Link Manager here!"}