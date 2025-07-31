from sqlalchemy import Column, Integer, String
from config import Base



class Visitors(Base):
    __tablename__ = 'Visitors'
    VisitorID = Column(Integer, primary_key=True)
    VisitorName = Column(String)
