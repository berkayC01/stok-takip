from fastapi import FastAPI
from .routers import items

app = FastAPI(title="Stok Takip API")

app.include_router(items.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to Stok Takip API"}
