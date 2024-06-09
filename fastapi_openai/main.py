from fastapi import FastAPI
from pydantic import BaseModel
from utils import getPrompt
# Initialize FastAPI
app = FastAPI()

# Define your data model for Product
class Order(BaseModel):
    product: str
    units: int

class Product(BaseModel):
    name: str
    notes: str

"""

@app.get("/ok")
async def ok_endpoint():
    return {"message": "ok"}

@app.get("/hello")
async def hello_endpoint(name: str = 'World'):
    return {"message": f"Hello, {name}!"}

@app.post("/orders")
async def place_order_with_units(product: str, units: int):
    return {"message": f"Order for {units} units of {product} placed successfully."}

@app.post("/orders_pydantic")
async def place_order(order: Order):
    return {"message": f"Order for {order.units} units of {order.product} placed successfully."}


@app.post("/product_description")
async def generate_product_description(product: Product):
    description = getPrompt(f"Product name: {product.name}, Notes: {product.notes}")
    return {"product_description": description}
    
"""


@app.post("/get_llm_response")
async def generate_product_description(prompt: str):
    reply = getPrompt(f"Prompt: {prompt}")
    return {"Reply": reply}