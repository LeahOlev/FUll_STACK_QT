from sqlalchemy import Column, Integer, String
from config import Base



class VisitorPerAttraction(Base):
    __tablename__ = 'VisitorPerAttraction'
    VisitorPerAttractionID = Column(Integer, primary_key=True)
    VisitorID = Column(Integer)
    AttractionId = Column(Integer)
