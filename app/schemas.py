from pydantic import BaseModel

class CatBase(BaseModel):
    name: str
    color: str

class CatCreate(CatBase):
    pass

class Cat(CatBase):
    id: int

    class Config:
        orm_mode = True

class CatUpdate(BaseModel):
    name: str | None = None
    color: str | None = None


