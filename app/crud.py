from sqlalchemy.orm import Session

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

