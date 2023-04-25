# from . import crud, models, schemas
import crud
import models
import schemas
from database import SessionLocal, engine
from sqlalchemy.orm import Session

from fastapi import Depends, FastAPI, HTTPException

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/cats/", response_model=schemas.Cat)
def create_cat(cat: schemas.CatBase, db: Session = Depends(get_db)):
    """
    creates a cat in the db
    """
    return crud.create_cat(db=db, cat=cat)


@app.get("/cats/", response_model=list[schemas.Cat])
def read_cats(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Returns all cats stored in DB
    """
    cats = crud.get_cats(db, skip=skip, limit=limit)
    return cats


# Cat Detail
@app.get("/cats/{cat_id}", response_model=schemas.CatBase)
def read_cat(cat_id: int, db: Session = Depends(get_db)):
    """
    returns detailed information of a single cat
    """
    db_cat = crud.get_cat(db, cat_id=cat_id)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    return db_cat

@app.patch("/cats/{cat_id}", response_model=schemas.Cat)
def update_cat(cat_id: int, cat: schemas.CatUpdate, db: Session = Depends(get_db)):
    """
    returns detailed information of a single cat
    """
    return crud.update_cat(db, cat_id, cat)

@app.delete("/cats/{cat_id}", response_model=schemas.CatBase)
def delete_cat(cat_id: int, db: Session = Depends(get_db)):
    """
    returns detailed information of a single cat
    """
    return crud.delete_cat(db, cat_id)