from sqlalchemy import Column, Integer, String
from config import Base


class Users(Base):
    __tablename__ = 'Users'
    UserID = Column(Integer, primary_key=True)
    FirstName = Column(String)
    LastName = Column(String)
    Email = Column(String)
