from sqlalchemy.orm import Session

from . import models, schemas


def get_item(db: Session, name: int):
    return db.query(models.InventoryItem).filter(models.InventoryItem.name == name).first()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.InventoryItem).offset(skip).limit(limit).all()


def create_item(db: Session, item: schemas.Item):
    db_item = models.InventoryItem(item_id = item.item_id, name=item.name, price=item.price, brand=item.brand)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item