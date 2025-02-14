from typing import Union
from fastapi import FastAPI
import uvicorn  # Added import

Fastapp = FastAPI()

@Fastapp.get("/tut")  # Changed from "/" to "/tut"
def read_root():
    return {"Hello": "World"}

@Fastapp.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    uvicorn.run("app:Fastapp", host="127.0.0.1", port=8000, reload=True)

