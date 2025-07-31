from config import Session
from models.Attractions import Attractions

class AttractionsRepository:
    def get_all(self):
        session = Session()
        try:
            return session.query(Attractions).all()
        finally:
            session.close()

    def get_by_id(self, attraction_id):
        session = Session()
        try:
            return session.query(Attractions).filter_by(id=attraction_id).first()
        finally:
            session.close()

    def add(self, attraction):
        session = Session()
        try:
            session.add(attraction)
            session.commit()
        finally:
            session.close()

    def update(self, attraction_id, updated):
        session = Session()
        try:
            attraction = session.query(Attractions).filter_by(id=attraction_id).first()
            if not attraction:
                return None
            for attr in vars(updated):
                if attr.startswith("_"):
                    continue
                setattr(attraction, attr, getattr(updated, attr))
            session.commit()
            return attraction
        finally:
            session.close()

    def delete(self, attraction_id):
        session = Session()
        try:
            attraction = session.query(Attractions).filter_by(id=attraction_id).first()
            if not attraction:
                return None
            session.delete(attraction)
            session.commit()
            return attraction
        finally:
            session.close()
    def exists_by_name(self, name):
        session = Session()
        return session.query(Attractions).filter_by(name=name).first() is not None




#from models.Attractions import Attractions
#from sqlalchemy.orm import Session
#
#
#class AttractionsRepository:
#    def __init__(self):
#        self.session = Session()
#
#    def add(self, attraction: Attractions):
#        self.session.add(attraction)
#        self.session.commit()
#
#    def get_all(self):
#        return self.session.query(Attractions).all()
#
#    def get_by_id(self, AttractionID):
#        return self.session.query(Attractions).get(AttractionID)
#
#    def update(self, AttractionID, new_data: Attractions):
#        attractionId = self.get_by_id(AttractionID)
#        if attractionId:
#            attractionId.AttractionID = new_data.AttractionID
#            attractionId.Lat = new_data.Lat
#            attractionId.Lng = new_data.Lng
#            attractionId.RegionID = new_data.RegionId
#            attractionId.AttractionName = new_data.AttractionName
#            attractionId.OpeningHours = new_data.openingHours
#            attractionId.ClosingHours = new_data.closingHours
#            attractionId.DurationMax = new_data.DurationMax
#            attractionId.Price = new_data.Price
#            attractionId.DescriptionLink = new_data.DescriptionLink
#            attractionId.AttractionTypeID = new_data.AttractionTypeID
#            self.session.commit()
#        return attractionId
#
#    def delete(self, AttractionID):
#        attractionId = self.get_by_id(AttractionID)
#        if attractionId:
#            self.session.delete(attractionId)
#            self.session.commit()
#        return attractionId
#
#    def exists_by_name(self, name):
#        return self.session.query(Attractions).filter_by(name=name).first() is not None
#