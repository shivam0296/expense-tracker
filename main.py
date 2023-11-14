"""
The Main purpose of this file is to run the Flask App server to support the expense tracker app frontend
"""


from typing import Union

from fastapi import FastAPI
from utilities import Utilities 

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/get_all")
def get_all():
    utl = Utilities()
    res = utl.get_all_data()
    return res

