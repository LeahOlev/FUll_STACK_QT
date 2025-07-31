from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from config import Base



class SavedTravels(Base):
    __tablename__ = 'SavedTravel'
    SavedTravelId = Column(Integer, primary_key=True)
    TraelID = Column(Integer)
    AttractionId= Column(Integer)
    Timetable= Column(Integer)
