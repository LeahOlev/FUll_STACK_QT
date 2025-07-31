from models.AttractionType import AttractionType
from sqlalchemy.orm import Session


class AttractionTypeRepository:
    def __init__(self):
        self.session = Session()

    def add(self, type: AttractionType):
        self.session.add(type)
        self.session.commit()

    def get_all(self):
        return self.session.query(AttractionType).all()

    def get_by_id(self, AttractionTypeID):
        return self.session.query(AttractionType).get(AttractionTypeID)

    def update(self, AttractionTypeID, new_data: AttractionType):
        typeId = self.get_by_id(AttractionType.AttractionTypeID)
        if typeId:
            typeId.TypeName = new_data.TypeName
            typeId.AttractionTypeID = new_data.AttractionTypeID
            self.session.commit()
        return type

    def delete(self, AttractionTypeID):
        typeId = self.get_by_id(AttractionTypeID)
        if typeId:
            self.session.delete(typeId)
            self.session.commit()
        return typeId

    def exists_by_name(self, name):
        session = Session()
        return session.query(AttractionType).filter_by(name=name).first() is not None
