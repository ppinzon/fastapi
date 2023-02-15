from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Cat(Base):
    __tablename__ = 'cats'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False)
    color = Column(String, unique=False)