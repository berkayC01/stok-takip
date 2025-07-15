from enum import Enum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="STOCKERRA")

# Placeholder in-memory storage
products_db = {}
transactions_db = []


class Product(BaseModel):
    id: int
    name: str
    category: str
    brand: str
    barcode: str
    skt: str
    stock_level: int = 0


class ProductCreate(BaseModel):
    name: str
    category: str
    brand: str
    barcode: str
    skt: str


class TransactionType(str, Enum):
    IN = "IN"
    OUT = "OUT"
    TRANSFER = "TRANSFER"


class StockTransaction(BaseModel):
    product_id: int
    quantity: int
    type: TransactionType


@app.post("/products/", response_model=Product)
async def create_product(product: ProductCreate):
    product_id = len(products_db) + 1
    prod = Product(id=product_id, **product.dict())
    products_db[product_id] = prod
    return prod


@app.get("/products/", response_model=List[Product])
async def list_products():
    return list(products_db.values())


@app.post("/stocks/transactions", response_model=StockTransaction)
async def add_transaction(transaction: StockTransaction):
    if transaction.product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    if transaction.quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be positive")

    transactions_db.append(transaction)
    prod = products_db[transaction.product_id]
    if transaction.type == TransactionType.IN:
        prod.stock_level += transaction.quantity
    elif transaction.type == TransactionType.OUT:
        prod.stock_level -= transaction.quantity
    # TRANSFER does not change stock level in this simple example
    return transaction


@app.get("/stocks/transactions", response_model=List[StockTransaction])
async def list_transactions():
    return transactions_db
