from sqlalchemy.orm import Session
from config import Session
from models.Visitors import Visitors

class VisitorRepository:
    def get_all(self):
        session = Session()
        try:
            return session.query(Visitors).all()
        finally:
            session.close()

    def get_by_id(self, id):
        session = Session()
        try:
            return session.query(Visitors).filter_by(id=id).first()
        finally:
            session.close()

    def add(self, visitor):
        session = Session()
        try:
            session.add(visitor)
            session.commit()
        finally:
            session.close()

    def update(self, id, updated):
        session = Session()
        try:
            visitor = session.query(Visitors).filter_by(id=id).first()
            if not visitor:
                return None
            for attr in vars(updated):
                if attr.startswith("_"):
                    continue
                setattr(visitor, attr, getattr(updated, attr))
            session.commit()
            return visitor
        finally:
            session.close()

    def delete(self, id):
        session = Session()
        try:
            visitor = session.query(Visitors).filter_by(id=id).first()
            if visitor:
                session.delete(visitor)
                session.commit()
            return visitor
        finally:
            session.close()

    def exists_by_name(self, name):
        session = Session()
        return session.query(Visitors).filter_by(name=name).first() is not None
