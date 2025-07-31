from sqlalchemy import Column, Integer, String
from config import Base



class AttractionType(Base):
    __tablename__ = 'AttractionType'
    AttractionTypeID = Column(Integer, primary_key=True)
    TypeName = Column(String)
