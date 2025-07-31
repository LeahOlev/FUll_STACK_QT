from config import Base
from sqlalchemy import Column, Integer, String

class Region(Base):
    __tablename__ = 'Region'

    RegionID = Column(Integer, primary_key=True)
    RegionName = Column(String)
