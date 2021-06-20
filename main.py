from fastapi import FastAPI, Path, Query, HTTPException, Depends
import models
from schemas import *
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

#intiialised the db
models.Base.metadata.create_all(bind=engine)

inventory = {
}

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()


@app.get("/")
def home():
    return inventory

# @app.post("/create-item/{item_id}")
# def create_item(item_id: int, item: Item, db: Session = Depends(get_db)):
#     if item_id in inventory:
#         return {"Error": "Item already exists"}
#     inventory[item_id] = item
#     return inventory

@app.post("/create-item")
def create_item(request: Item, db: Session = Depends(get_db)):
    new_item = models.InventoryItem(item_id=request.item_id, name=request.name, price=request.price, brand=request.brand)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return "Success"


@app.get("/get-total-price-by-name")
def get_item(*, name: str = Query(None, title="Name", description="Name of the item"), amount: int = 1):
    if name:
        for item_id in inventory:
            if inventory[item_id].name == name:
                return inventory[item_id].price * amount
        raise HTTPException(status_code=404, detail="Not Found: available Items: " + str([inventory[item_id].name for item_id in inventory]))
    return {"Data": "No Name given, available Items: " + str([inventory[item_id].name for item_id in inventory])}

#TODO - Validate items by name to ensure no duplication of item name.

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id in inventory:
        if item.name != None:
           inventory[item_id].name = item.name
        if item.price != None:
           inventory[item_id].price = item.price
        if item.brand != None:
           inventory[item_id].brand = item.brand
        return inventory[item_id]
    raise HTTPException(status_code=404, detail=f"item_id {item_id} Not Found")

@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
    if item_id in inventory:
        del inventory[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"item_id {item_id} Not Found \n {inventory}")