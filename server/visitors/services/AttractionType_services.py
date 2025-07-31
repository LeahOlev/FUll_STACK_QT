from models.AttractionType import AttractionType
from repository.AttractionTypeRepository import AttractionTypeRepository
from dto.AttractionType_DTO import AttractionTypeDTO
from exceptions.exceptions import ItemNotFoundException

class AttractionTypeServices:
    def __init__(self, repo=None):
        self.repo = repo or AttractionTypeRepository()

    def add_AttractionType(self, dto: AttractionTypeDTO):
        item = AttractionType(**dto.dict())
        self.repo.add(item)

    def get_all_AttractionType(self):
        return self.repo.get_all()

    def get_AttractionType_by_id(self, id):
        item = self.repo.get_by_id(id)
        if not item:
            raise ItemNotFoundException(id)
        return item

    def update_AttractionType(self, id, dto: AttractionTypeDTO):
        updated = AttractionType(**dto.dict())

    def delete(self, id):
        result = self.repo.delete(id)
        if not result:
            raise ItemNotFoundException(id)