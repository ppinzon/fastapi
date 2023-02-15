from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

# from . import crud, models, schemas
import crud, models, schemas
from database import SessionLocal, engine

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
def create_cat(cat: schemas.CatCreate, db: Session = Depends(get_db)):
    # db_cat = crud.get_cat(db, id=cat.id)
    # if db_cat:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_cat(db=db, cat=cat)


@app.get("/cats/", response_model=list[schemas.Cat])
def read_cats(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cats = crud.get_cats(db, skip=skip, limit=limit)
    return cats


@app.get("/cats/{cat_id}", response_model=schemas.Cat)
def read_cat(cat_id: int, db: Session = Depends(get_db)):
    db_cat = crud.get_cat(db, cat_id=cat_id)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_cat
