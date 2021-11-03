from fastapi import FastAPI, Path
from typing import Optional

# api object
app = FastAPI()


# endpoint np. /hello, /get-item
# localhost/home = endpoint + url
# fb.com/create-user /create-user is endpoint for fb

# methods: GET (get, return info), POST (create, add sth new),
# PUT (update the data), DELETE


@app.get("/")
# root endpoint above function that triggers it
def home():
    return {"Data": "Test"}


# py dict is converted into json
# whenever u return info from endpoint, the info is in json


# uvicorn myapp1:app --reload
# http://127.0.0.1:8000/docs DOCS

@app.get("/about")
def about():
    return {"Data": "About"}


# path parameters / endpoint parameters

inventory = {
    1: {
        "name": "Milk",
        "price": 2.39,
        "brand": "regular"
    },
    2: {
            "name": "Juice",
            "price": 3.49,
            "brand": "apple"
        }
}


@app.get("/get-item/{item_id}")
# def sth (parameter:type hint)
def get_item(item_id: int):
    return inventory[item_id]

# http://127.0.0.1:8000/get-item/1


@app.get("/get-item/{item_id}/{name}")
# def sth (parameter:type hint)
def get_item(item_id: int, name: str = None):
    return inventory[item_id]


@app.get("/get-item/{item_id}")
# def sth (parameter:type hint)
def get_item(item_id: int = Path(None, description="The ID of the item you'd like to view", ge=1)):
    # None is default, so if you dont pass anything as item_id, it will be default as None
    # description in the docs
    return inventory[item_id]


# query parameters
# fb.com/home/?redirect=martyna&msg=fail@"
# ?sth=/sth" is query

@app.get("/get-by-name")
def get_item(name: str):
    # query parameter is required
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}


# lsof -i :8000
# kill -9 9481 (pid)

@app.get("/get-by-name")
def get_item(test: int, name: Optional[str] = None):
    # bc None - query param is optional
    # from typing import Optional
    # def get_item(*, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}

