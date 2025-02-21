import datetime
from sqlalchemy import Column, DateTime, Integer, String
from .database import BaseDatabase


class User(BaseDatabase):
    __tablename__ = "users"
    name = Column(String)
