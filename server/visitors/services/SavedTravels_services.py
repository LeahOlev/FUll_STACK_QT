from models.SavedTravels import SavedTravels
from repository.SavedTravelsRepository import SavedTravelsRepository
from dto.SavedTravels_DTO import SavedTravelsDTO
from exceptions.exceptions import ItemNotFoundException

class SavedTravelsServices:
    def __init__(self, repo=None):
        self.repo = repo or SavedTravelsRepository()

    def add(self, dto: SavedTravelsDTO):
        item = SavedTravels(**dto.dict())
        self.repo.add(item)

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id):
        item = self.repo.get_by_id(id)
        if not item:
            raise ItemNotFoundException(id)
        return item

    def update(self, id, dto: SavedTravelsDTO):
        updated = SavedTravels(**dto.dict())
        result = self.repo.update(id, updated)
        if not result:
            raise ItemNotFoundException(id)
        return result

    def delete(self, id):
        result = self.repo.delete(id)
        if not result:
            raise ItemNotFoundException(id)
