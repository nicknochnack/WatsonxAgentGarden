from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()

class Item(BaseModel):
    quote_price: int
    name: str
    dob: str

@app.post("/")
async def root(item:Item):
    item_dict = item.model_dump()
    return {"message": "New policy created", "data":{
        "premium":item_dict['quote_price'],
        "name":item_dict['name'].title(),
        "dob":item_dict['dob'].title(),
        }}