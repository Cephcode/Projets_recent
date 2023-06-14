from fastapi import FastAPI,Response
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
app = FastAPI()

products = [
    {"id": 1, "name": "iPad", "price": 599},
    {"id": 2, "name": "iPhone", "price": 999},
    {"id": 3, "name": "iWatch", "price": 699},
]


@app.get("/products")
def index(response:Response):
    if products:
        response.status_code=200
    return products,response.status_code
@app.get("/products/search/{name}")
def search(name:str,response:Response):
    for product in products:
        if name in product.get("name"):
            return product
        else:
            response.status_code=404 
            return response
@app.get("/products/{id}")
def get_product(id: int, response:Response):
    for product in products:
        if product.get("id")==id:
            return product
@app.post ("/products")
def create_product(new_product: Product, response: Response):
    product = new_product.dict()
    product["id"] = len(products) + 1
    products.append(product)
    response.status_code = 200
    return product