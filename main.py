from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for the item

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

# Define a Post endpoint to create an item and a Get endpoint to read items

@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


# Define a Get endpoint to read items

@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]

# 1111111
# 2222222
