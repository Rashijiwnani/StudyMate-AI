from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String


class Base(DeclarativeBase):
    pass  


class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(255), unique=True)
    password = Column(String(255))