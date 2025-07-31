from sqlalchemy import Column, Integer, String
from config import Base



class TravelPerUser(Base):
    __tablename__ = 'TravelPerUser'
    TravelPerUserID = Column(Integer, primary_key=True)
    UserID = Column(Integer)
