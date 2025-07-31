from models.Attractions import Attractions
from repository.AttractionsRepository import AttractionsRepository
from dto.Attractions_DTO import AttractionsDTO
from exceptions.exceptions import ItemAlreadyExistsException, ItemNotFoundException

class AttractionsServices:
    def __init__(self):
        self.repo = AttractionsRepository()

    def add_attraction(self, dto: AttractionsDTO):
        if self.repo.get_by_id(dto.id):
            raise ItemAlreadyExistsException(dto.id)
        attraction = Attractions(**dto.dict())
        self.repo.add(attraction)

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id):
        item = self.repo.get_by_id(id)
        if not item:
            raise ItemNotFoundException(id)
        return item

    def update(self, id, dto: AttractionsDTO):
        updated = Attractions(**dto.dict())
        result = self.repo.update(id, updated)
        if not result:
            raise ItemNotFoundException(id)
        return result

    def delete(self, id):
        result = self.repo.delete(id)
        if not result:
            raise ItemNotFoundException(id)
