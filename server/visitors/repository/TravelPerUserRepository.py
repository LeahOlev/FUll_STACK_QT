from sqlalchemy.orm import Session
from config import Session
from models.TravelPerUser import TravelPerUser

class TravelPerUserRepository:
    def get_all(self):
        session = Session()
        try:
            return session.query(TravelPerUser).all()
        finally:
            session.close()

    def get_by_id(self, id):
        session = Session()
        try:
            return session.query(TravelPerUser).filter_by(id=id).first()
        finally:
            session.close()

    def add(self, item):
        session = Session()
        try:
            session.add(item)
            session.commit()
        finally:
            session.close()

    def update(self, id, updated):
        session = Session()
        try:
            item = session.query(TravelPerUser).filter_by(id=id).first()
            if not item:
                return None
            for attr in vars(updated):
                if attr.startswith("_"):
                    continue
                setattr(item, attr, getattr(updated, attr))
            session.commit()
            return item
        finally:
            session.close()

    def delete(self, id):
        session = Session()
        try:
            item = session.query(TravelPerUser).filter_by(id=id).first()
            if item:
                session.delete(item)
                session.commit()
            return item
        finally:
            session.close()

    def exists_by_UserID(self, UserID):
        session = Session()
        return session.query(TravelPerUser).filter_by(UserID=UserID).first() is not None
