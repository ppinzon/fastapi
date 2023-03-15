from sqlalchemy.orm import Session
from fastapi import Response
import models, schemas

def get_cat(db: Session, cat_id: int):
    return db.query(models.Cat).filter(models.Cat.id == cat_id).first()

def get_cats(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cat).offset(skip).limit(limit).all()

def create_cat(db: Session, cat: schemas.CatCreate):
    db_cat = models.Cat(name=cat.name, color=cat.color)
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat

def update_cat(db: Session, cat_id: int, cat: schemas.CatUpdate):
    db_query = db.query(models.Cat).filter(models.Cat.id == cat_id)
    db_cat = db_query.first()
    
    update_data = cat.dict(exclude_unset=True)
    db_query.filter(models.Cat.id == cat_id).update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(db_cat)
    return db_cat

def delete_cat(db: Session, cat_id: int):
    db_cat = db.query(models.Cat).filter(models.Cat.id == cat_id).first()

    db.delete(db_cat)
    db.commit()
    return Response("record deleted", status_code=204,)