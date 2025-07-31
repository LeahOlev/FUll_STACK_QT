import sqlalchemy

from sqlalchemy import Column, Integer, String
from config import Base


class Attractions(Base):
    __tablename__ = 'Attractions'
    AttractionID = Column(Integer, primary_key=True)
    Lat = Column(String)
    Lng = Column(String)
    RegionId = Column(Integer)
    AttractionName = Column(String)
    openingHours = Column(String)
    closingHours = Column(String)
    DurationMax = Column(Integer)
    Price = Column(Integer)
    DescriptionLink = Column(String)
    AttractionTypeID = Column(Integer)
