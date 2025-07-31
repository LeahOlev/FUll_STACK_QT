from config import Session
from models.Region import Region
from sqlalchemy.orm import Session


class RegionRepository:

    def get_all(self):
        session = Session()
        try:
            return session.query(Region).all()
        finally:
            session.close()

    def get_by_id(self, id):
        session = Session()
        try:
            return session.query(Region).filter_by(id=id).first()
        finally:
            session.close()

    def add(self, region):
        session = Session()
        try:
            session.add(region)
            session.commit()
        finally:
            session.close()

    def update(self, RegionID, new_data: Region):
        regionID = self.get_by_id(RegionID)
        if regionID:
            regionID.RegionName = new_data.RegionName
            regionID.RegionID = new_data.RegionID
            self.session.commit()
        return regionID


    def delete(self, id):
        session = Session()
        try:
            region = session.query(Region).filter_by(id=id).first()
            if region:
                session.delete(region)
                session.commit()
            return region
        finally:
            session.close()

    def exists_by_name(self, name):
        session = Session()
        return session.query(Region).filter_by(name=name).first() is not None
