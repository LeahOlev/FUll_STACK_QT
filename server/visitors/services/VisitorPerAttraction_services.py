from models.VisitorPerAttraction import VisitorPerAttraction
from repository.VisitorPerAttractionRepository import VisitorPerAttractionRepository
from dto.VisitorPerAttraction_DTO import VisitorPerAttractionDTO
from exceptions.exceptions import ItemNotFoundException

class VisitorPerAttractionServices:
    def __init__(self, repo=None):
        self.repo = repo or VisitorPerAttractionRepository()

    def add(self, dto: VisitorPerAttractionDTO):
        item = VisitorPerAttraction(**dto.dict())
        self.repo.add(item)

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id):
        item = self.repo.get_by_id(id)
        if not item:
            raise ItemNotFoundException(id)
        return item

    def update(self, id, dto: VisitorPerAttractionDTO):
        updated = VisitorPerAttraction(**dto.dict())
        result = self.repo.update(id, updated)
        if not result:
            raise ItemNotFoundException(id)
        return result

    def delete(self, id):
        result = self.repo.delete(id)
        if not result:
            raise ItemNotFoundException(id)
